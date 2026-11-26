/* dogen — açılır menü, dil tercihi, saat (tüm sayfalar) */
(function () {
  "use strict";
  var root = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- Açılır menü ---- */
  var mn = document.getElementById("mn");
  var btn = document.querySelector(".mn-btn");
  if (mn && btn) {
    var panel = mn.querySelector(".mn-panel");
    var open = false, timer = 0;
    var focusables = function () {
      return Array.prototype.filter.call(panel.querySelectorAll("a[href], button:not([disabled])"), function (el) {
        return el.getClientRects().length > 0;
      });
    };
    var show = function () {
      if (open) return;
      open = true;
      clearTimeout(timer);
      mn.hidden = false;
      root.classList.add("mn-lock");
      if (window.lenis) window.lenis.stop();
      btn.setAttribute("aria-expanded", "true");
      void mn.offsetWidth; /* başlangıç durumunu uygula, sonra geçişi başlat */
      requestAnimationFrame(function () { mn.classList.add("is-open"); });
      var x = mn.querySelector(".mn-x");
      if (x) setTimeout(function () { x.focus({ preventScroll: true }); }, reduce ? 0 : 80);
    };
    var hide = function (returnFocus) {
      if (!open) return;
      open = false;
      mn.classList.remove("is-open");
      btn.setAttribute("aria-expanded", "false");
      timer = setTimeout(function () {
        mn.hidden = true;
        root.classList.remove("mn-lock");
        if (window.lenis) window.lenis.start();
      }, reduce ? 0 : 560);
      if (returnFocus !== false) btn.focus({ preventScroll: true });
    };
    btn.addEventListener("click", show);
    mn.addEventListener("click", function (e) {
      if (e.target.closest("[data-mn-close]")) { hide(); return; }
      var a = e.target.closest("a[href]");
      if (!a) return;
      var u = new URL(a.href, location.href);
      /* Aynı sayfadaki çapaya gidiyorsa menüyü kapat ve kaydır */
      if (u.origin === location.origin && u.pathname === location.pathname && u.hash) {
        e.preventDefault();
        hide(false);
        var t = document.getElementById(u.hash.slice(1));
        setTimeout(function () {
          if (!t) return;
          if (window.lenis) window.lenis.scrollTo(t, { offset: -80 });
          else t.scrollIntoView({ behavior: reduce ? "auto" : "smooth" });
        }, reduce ? 0 : 420);
      }
    });
    document.addEventListener("keydown", function (e) {
      if (!open) return;
      if (e.key === "Escape") { e.preventDefault(); hide(); return; }
      if (e.key !== "Tab") return;
      var f = focusables();
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && (document.activeElement === first || !panel.contains(document.activeElement))) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && (document.activeElement === last || !panel.contains(document.activeElement))) { e.preventDefault(); first.focus(); }
    });
    window.addEventListener("pageshow", function (e) { if (e.persisted && open) { open = true; hide(false); } });
  }

  /* ---- Dil bağlantıları: tercihi hatırla (ana sayfa yönlendirmesi buna bakar) ---- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[data-lang-link]");
    if (!a) return;
    try { localStorage.setItem("dogen-lang", a.getAttribute("data-lang-link")); } catch (err) {}
  });

  /* ---- Sevilla saati (iç sayfalar) ---- */
  var ck = document.querySelector("[data-clock]");
  if (ck && window.Intl) {
    var loc = root.lang === "es" ? "es-ES" : "tr-TR";
    var tick = function () {
      ck.textContent = new Intl.DateTimeFormat(loc, { timeZone: "Europe/Madrid", hour: "2-digit", minute: "2-digit" }).format(new Date());
    };
    tick();
    setInterval(tick, 15000);
  }

  document.querySelectorAll("[data-yr]").forEach(function (el) { el.textContent = String(new Date().getFullYear()); });
})();
