/* dogen.es — TR/ES. Türkçe metin HTML'den okunur; burada yalnızca İspanyolcası durur. */
(function () {
  "use strict";

  var ES = {
    _title: "dogen.es — Consultoría educativa y de relocalización en Sevilla",
    skip: "Saltar al contenido",
    nav_services: "Servicios", nav_process: "Proceso", nav_about: "Quiénes somos", nav_partners: "Centros", nav_contact: "Contacto",
    hero_kicker: "Consultoría educativa y de relocalización · Sevilla",
    hero_h1: "Orientación desde Sevilla para quien quiere estudiar en España.",
    hero_lead: "Escuela de español, Formación Profesional o universidad: decidimos contigo qué camino encaja y te acompañamos desde la matrícula y el expediente de visado hasta tu primer mes en España.",
    cta_wa: "Escríbenos por WhatsApp",
    arch_cap: "Motivo: azulejos de los patios sevillanos.",
    svc_h2: "Servicios",
    svc_p: "La mayoría empieza con un periodo de español y después pasa a FP o a la universidad. Por eso planificamos centro, documentación y llegada en un único calendario.",
    s1_t: "Escuela de español", s1_d: "Programas intensivos en centros acreditados por el Instituto Cervantes que cumplen los requisitos del visado de estudios.",
    s1_i: "Prueba de nivel, elección de centro, matrícula, orientación de alojamiento",
    s2_t: "Formación Profesional (FP)", s2_d: "Ciclos de Grado Superior de dos años, gratuitos, en centros públicos españoles.",
    s2_i: "Elección de ciclo y centro, homologación del título de bachillerato, calendario de admisión",
    s3_t: "Universidad", s3_d: "Acreditación UNEDasiss y solicitud a universidades públicas andaluzas a través del Distrito Único Andaluz (DUA).",
    s3_i: "Registro en UNEDasiss, preinscripción DUA, orden de preferencias",
    s4_t: "Llegada y asentamiento", s4_d: "Los trámites de las primeras semanas en España: todos con cita previa, todos en español.",
    s4_i: "Empadronamiento, certificado digital, cita de NIE / TIE",
    proc_h2: "Cómo funciona el proceso",
    proc_p: "Desde el principio está claro quién hace qué. La solicitud de visado la presentas tú personalmente, como exige la ley; que el expediente esté completo es cosa nuestra.",
    th_step: "Paso", th_us: "Nosotros", th_you: "Tú",
    r1: "Primera consulta", r1_us: "Escuchamos tu situación y te explicamos las rutas posibles.", r1_you: "Nos cuentas tu objetivo, tu presupuesto y los documentos que tienes.",
    r2: "Plan de ruta", r2_us: "Preparamos por escrito las opciones de centro y programa, con su calendario.", r2_you: "Eliges tu ruta.",
    r3: "Admisión y documentos", r3_us: "Gestionamos la matrícula y la lista de traducciones, apostillas y homologaciones.", r3_you: "Consigues los documentos en Turquía.",
    r4: "Visado", r4_us: "Revisamos el expediente consular y planificamos la cita.", r4_you: "Presentas la solicitud en persona.",
    r5: "Primeros 30 días", r5_us: "Te acompañamos en el empadronamiento, el certificado digital y el NIE/TIE.", r5_you: "Llegas a Sevilla.",
    ab_h2: "Quiénes somos",
    ab_p1: "dogen.es es una consultoría educativa y de relocalización fundada en Sevilla por Fırat Daşdöğen. Trabajamos de forma individual con personas de Turquía que quieren venir a estudiar a España; no vendemos paquetes, miramos cada expediente con sus propias circunstancias.",
    ab_p2: "En España todo avanza con citas, documentos y plazos. Un papel que falta o una fecha perdida pueden suponer meses de retraso. Por eso gran parte de nuestro trabajo es discreto y minucioso: el documento correcto, en el orden correcto, a tiempo.",
    ab_name: "¿De dónde viene el nombre? En japonés «dō» significa camino, y coincide con el apellido de nuestro fundador.",
    pa_h2: "Para escuelas y centros",
    pa_p: "Colaboramos por escrito y con facturación oficial con academias de idiomas y centros educativos en España. Hacemos una evaluación previa de los candidatos en turco y preparamos y seguimos expedientes completos.",
    faq_h2: "Preguntas frecuentes",
    q1: "No hablo español, ¿puedo empezar igualmente?", a1: "Sí. La mayoría de las rutas empiezan con un periodo en una escuela de español; te recomendamos centro y programa según tu nivel y tu objetivo.",
    q2: "¿Presentáis vosotros la solicitud de visado?", a2: "No. La presentas tú personalmente, como exige la ley. Nosotros nos encargamos de que el expediente esté completo y correcto, y de planificar citas y plazos. La decisión final corresponde a las autoridades españolas.",
    q3: "¿Cómo se determina el precio?", a3: "Según la ruta y el alcance del servicio. Te lo enviamos por escrito después de la primera consulta.",
    q4: "¿Podemos hablar mientras sigo en Turquía?", a4: "Claro. La primera consulta la hacemos por WhatsApp o videollamada; cuando llegues a Sevilla también podemos vernos en la oficina.",
    ct_h2: "Contacto",
    ct_p: "Cuéntanos brevemente tu objetivo y tu calendario y te respondemos. Puedes escribir en turco o en español.",
    c1: "Estudiantes", c2: "Escuelas y centros", c3: "Teléfono y WhatsApp", c4: "Oficina", c5: "Hora en Sevilla",
    row_cta: "Escríbenos sobre esta ruta",
    legal: "dogen.es es una consultoría educativa y de relocalización independiente. Las solicitudes de visado y residencia las presenta personalmente el interesado; su resolución corresponde a las autoridades españolas."
  };

  var TR = { _title: document.title };
  var els = document.querySelectorAll("[data-i18n]");
  els.forEach(function (el) { TR[el.dataset.i18n] = el.textContent; });
  var DICT = { tr: TR, es: ES };
  var root = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var lang = "tr";
  var WA = "https://wa.me/34666104496";
  var WA_MSG = {
    tr: function (s) { return "Merhaba, " + s + " hakkında bilgi almak istiyorum."; },
    es: function (s) { return "Hola, me gustaría recibir información sobre: " + s + "."; }
  };

  /* ---- Başlık: kelime kelime ---- */
  function splitWords(el) {
    var text = el.textContent.trim();
    el.setAttribute("aria-label", text);
    el.classList.remove("is-in");
    el.innerHTML = text.split(/\s+/).map(function (w, i) {
      var safe = w.replace(/&/g, "&amp;").replace(/</g, "&lt;");
      return '<span class="w" aria-hidden="true"><span style="--i:' + i + '">' + safe + "</span></span>";
    }).join(" ");
    requestAnimationFrame(function () { requestAnimationFrame(function () { el.classList.add("is-in"); }); });
  }

  /* ---- Dil ---- */
  function setLang(next) {
    var d = DICT[next] || TR;
    lang = next;
    root.lang = next;
    document.title = d._title;
    els.forEach(function (el) { var v = d[el.dataset.i18n]; if (v) el.textContent = v; });
    document.querySelectorAll(".split").forEach(splitWords);
    document.querySelectorAll(".steps td:nth-child(2)").forEach(function (td) { td.dataset.label = d.th_us; });
    document.querySelectorAll(".steps td:nth-child(3)").forEach(function (td) { td.dataset.label = d.th_you; });
    document.querySelectorAll(".row-link").forEach(function (a) {
      a.href = WA + "?text=" + encodeURIComponent(WA_MSG[next](d[a.dataset.svc]));
    });
    document.querySelectorAll(".lang button").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.lang === next));
    });
    tick();
    try { localStorage.setItem("dogen-lang", next); } catch (e) {}
  }

  document.querySelectorAll(".lang button").forEach(function (b) {
    b.addEventListener("click", function () {
      if (b.dataset.lang === lang) return;
      if (reduce) { setLang(b.dataset.lang); return; }
      root.classList.add("is-swapping");
      setTimeout(function () { setLang(b.dataset.lang); root.classList.remove("is-swapping"); }, 180);
    });
  });

  /* ---- Sevilla saati ---- */
  var timeEl = document.getElementById("sev-time");
  var diffEl = document.getElementById("sev-diff");
  function minutesIn(tz, now) {
    var parts = new Intl.DateTimeFormat("en-GB", { timeZone: tz, hour: "2-digit", minute: "2-digit", hourCycle: "h23" }).formatToParts(now);
    var h = +parts.find(function (p) { return p.type === "hour"; }).value;
    var m = +parts.find(function (p) { return p.type === "minute"; }).value;
    return h * 60 + m;
  }
  function tick() {
    if (!timeEl) return;
    var now = new Date();
    timeEl.textContent = new Intl.DateTimeFormat(lang === "es" ? "es-ES" : "tr-TR", { timeZone: "Europe/Madrid", hour: "2-digit", minute: "2-digit" }).format(now);
    var diff = minutesIn("Europe/Istanbul", now) - minutesIn("Europe/Madrid", now);
    if (diff > 720) diff -= 1440; if (diff < -720) diff += 1440;
    var h = Math.round(diff / 60);
    diffEl.textContent = h === 0 ? (lang === "es" ? "Misma hora que en Turquía" : "Türkiye ile aynı saat")
      : (lang === "es" ? h + " h menos que en Turquía" : "Türkiye’den " + h + " saat geride");
  }
  setInterval(tick, 15000);

  /* ---- İlk dil ---- */
  var initial = "tr";
  try {
    var q = new URLSearchParams(location.search).get("lang");
    var saved = localStorage.getItem("dogen-lang");
    if (q === "es" || q === "tr") initial = q;
    else if (saved === "es" || saved === "tr") initial = saved;
    else if (/^es\b/i.test(navigator.language || "")) initial = "es";
  } catch (e) {}
  setLang(initial);

  /* ---- Başlık çubuğu: aşağı kaydırınca gizlen, yukarıda geri gel ---- */
  var header = document.querySelector(".site-header");
  var lastY = window.scrollY;

  /* ---- Süreç tablosu ---- */
  var table = document.querySelector(".steps");
  var bar = document.querySelector(".steps-bar span");
  var rows = table ? Array.prototype.slice.call(table.querySelectorAll("tbody tr")) : [];
  if (table && !reduce) root.classList.add("js-steps");

  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      ticking = false;
      var y = window.scrollY;
      if (!reduce) header.classList.toggle("is-hidden", y > 240 && y > lastY + 2);
      if (y < lastY - 2 || y < 240) header.classList.remove("is-hidden");
      lastY = y;

      if (!table) return;
      var vh = window.innerHeight, line = vh * 0.6;
      var r = table.getBoundingClientRect();
      var p = Math.min(1, Math.max(0, (line - r.top) / r.height));
      bar.parentNode.style.setProperty("--p", p.toFixed(3));
      var active = -1;
      rows.forEach(function (tr, i) { if (tr.getBoundingClientRect().top < line) active = i; });
      rows.forEach(function (tr, i) {
        tr.classList.toggle("is-active", i === active);
        tr.classList.toggle("is-done", i < active);
      });
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);
  onScroll();

  /* ---- Menü: aktif bölüm + başlık çizgileri ---- */
  if ("IntersectionObserver" in window) {
    var links = {};
    document.querySelectorAll(".nav a").forEach(function (a) { links[a.getAttribute("href").slice(1)] = a; });
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        Object.keys(links).forEach(function (k) { links[k].classList.toggle("is-current", k === en.target.id); });
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    Object.keys(links).forEach(function (id) { var s = document.getElementById(id); if (s) spy.observe(s); });

    var h2o = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("is-in"); h2o.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -15% 0px" });
    document.querySelectorAll(".block h2").forEach(function (h) { h2o.observe(h); });
  } else {
    document.querySelectorAll(".block h2").forEach(function (h) { h.classList.add("is-in"); });
  }

  /* ---- Çini karolar: dalga, dokunuşla dönme ---- */
  (function tiles() {
    var g = document.getElementById("tiles");
    var arch = document.getElementById("arch");
    if (!g || !arch) return;
    var NS = "http://www.w3.org/2000/svg", S = 88, COLS = 5, ROWS = 7;
    var corner = '<g fill="#f6f4ef" fill-opacity=".85"><path d="M0 0h11L0 11Z"/><path d="M88 0H77l11 11Z"/><path d="M0 88h11L0 77Z"/><path d="M88 88H77l11-11Z"/></g>';
    var star = '<g class="rot"><g transform="translate(44 44)" fill="none" stroke="#f6f4ef" stroke-width="1.6">' +
      '<rect x="-22" y="-22" width="44" height="44"/><rect x="-22" y="-22" width="44" height="44" transform="rotate(45)"/>' +
      '<circle r="9" stroke="#e2b764"/><circle class="dot" r="3.5" fill="#e2b764" stroke="none"/></g></g>';
    var list = [];
    var html = "";
    for (var r = 0; r < ROWS; r++) for (var c = 0; c < COLS; c++) {
      html += '<g class="tile' + (reduce ? "" : " pre") + '" data-r="' + r + '" data-c="' + c + '" transform="translate(' + c * S + " " + r * S + ')">' +
        '<rect class="hit" width="88" height="88" fill="#1f4a7a"/><path d="M.5.5h87v87H.5z" fill="none" stroke="#f6f4ef" stroke-opacity=".14"/>' + corner + star + "</g>";
    }
    g.innerHTML = html;
    var fb = document.getElementById("tile-fallback"); if (fb) fb.remove();
    g.querySelectorAll(".tile").forEach(function (t) { list.push({ el: t, rot: t.querySelector(".rot"), r: +t.dataset.r, c: +t.dataset.c, a: 0, last: 0 }); });
    if (reduce) return;

    var ready = false;
    list.forEach(function (t) {
      setTimeout(function () { t.el.classList.remove("pre"); }, 250 + (t.r + t.c) * 70);
    });
    setTimeout(function () { ready = true; }, 250 + (ROWS + COLS) * 70 + 900);

    function spin(t) {
      var now = performance.now();
      if (!ready || now - t.last < 950) return;
      t.last = now; t.a += 90;
      t.rot.style.transform = "rotate(" + t.a + "deg)";
      t.el.classList.add("hot");
      setTimeout(function () { t.el.classList.remove("hot"); }, 900);
    }
    g.addEventListener("pointerover", function (e) {
      var el = e.target.closest && e.target.closest(".tile");
      if (!el) return;
      spin(list[+el.dataset.r * COLS + +el.dataset.c]);
    });

    var visible = true;
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }).observe(arch);
    }
    setInterval(function () {
      if (!visible || document.hidden || !ready) return;
      var o = list[Math.floor(Math.random() * list.length)];
      list.forEach(function (t) {
        var d = Math.abs(t.r - o.r) + Math.abs(t.c - o.c);
        setTimeout(function () { spin(t); }, d * 90);
      });
    }, 7000);
  })();

  var yr = document.getElementById("yr");
  if (yr) yr.textContent = String(new Date().getFullYear());
})();
