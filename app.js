/* dogen.es — v3.1 TR/ES + Lenis & Katmanlı Hareket Motoru */
(function () {
  "use strict";

  var ES = {
    _title: "dogen.es — Consultoría educativa y de relocalización en Sevilla",
    skip: "Saltar al contenido",
    nav_services: "Servicios", nav_process: "Proceso", nav_about: "Quiénes somos", nav_partners: "Centros", nav_contact: "Contacto",
    hero_h1: "Orientación desde Sevilla para quien quiere estudiar en España.",
    hero_lead: "Escuela de español, Formación Profesional o universidad: decidimos contigo qué camino encaja y te acompañamos desde la matrícula y el expediente de visado hasta tu primer mes en España.",
    cta_wa: "Escríbenos por WhatsApp",
    m1_b: "1 a 1 desde Sevilla", m1_s: "Sin paquetes estándar, expediente a medida",
    m2_b: "FP pública · 0 €", m2_s: "Grado Superior presencial de 2 años",
    m3_b: "Primeros 30 días", m3_s: "Padrón, certificado digital y cita TIE",
    arch_cap: "Motivo: azulejos de los patios sevillanos.",
    arch_hint: "Pasa el cursor",
    mq_1: "escuela de español", mq_2: "formación profesional", mq_3: "universidad pública", mq_4: "asentamiento en sevilla",
    svc_tag: "01 — Rutas educativas",
    svc_h2: "Servicios",
    svc_p: "La mayoría empieza con un periodo de español y después pasa a FP o a la universidad. Por eso planificamos centro, documentación y llegada en un único calendario.",
    s1_t: "Escuela de español", s1_d: "Programas intensivos en centros acreditados por el Instituto Cervantes que cumplen los requisitos del visado de estudios.",
    s1_i: "Prueba de nivel · elección de centro · matrícula · orientación de alojamiento",
    s2_t: "Formación Profesional (FP)", s2_d: "Ciclos de Grado Superior de dos años, gratuitos, en centros públicos españoles con permiso de trabajo de hasta 30 h/semana.",
    s2_i: "Elección de ciclo y centro · homologación de bachillerato · calendario de admisión",
    s3_t: "Universidad", s3_d: "Acreditación UNEDasiss y solicitud a universidades públicas andaluzas a través del Distrito Único Andaluz (DUA).",
    s3_i: "Registro en UNEDasiss · preinscripción DUA · orden de preferencias",
    s4_t: "Llegada y asentamiento", s4_d: "Los trámites de las primeras semanas en España: todos con cita previa, todos en español.",
    s4_i: "Empadronamiento · certificado digital FNMT · cita de NIE / TIE",
    proc_tag: "02 — Cómo trabajamos",
    proc_h2: "Cómo funciona el proceso",
    proc_p: "Desde el principio está claro quién hace qué. La solicitud de visado la presentas tú personalmente, como exige la ley; que el expediente esté completo es cosa nuestra.",
    th_step: "Paso", th_us: "Nosotros", th_you: "Tú", th_map: "Flujo",
    r1: "Primera consulta", r1_us: "Escuchamos tu situación y te explicamos las rutas posibles.", r1_you: "Nos cuentas tu objetivo, tu presupuesto y los documentos que tienes.",
    r2: "Plan de ruta", r2_us: "Preparamos por escrito las opciones de centro y programa, con su calendario.", r2_you: "Eliges tu ruta.",
    r3: "Admisión y documentos", r3_us: "Gestionamos la matrícula y la lista de traducciones, apostillas y homologaciones.", r3_you: "Consigues los documentos en Turquía.",
    r4: "Visado", r4_us: "Revisamos el expediente consular y planificamos la cita.", r4_you: "Presentas la solicitud en persona.",
    r5: "Primeros 30 días", r5_us: "Te acompañamos en el empadronamiento, el certificado digital y el NIE/TIE.", r5_you: "Llegas a Sevilla.",
    ab_tag: "03 — En Sevilla",
    ab_h2: "Quiénes somos",
    ab_p1: "dogen.es es una consultoría educativa y de relocalización fundada en Sevilla por Fırat Daşdöğen. Trabajamos de forma individual con personas de Turquía que quieren venir a estudiar a España; no vendemos paquetes, miramos cada expediente con sus propias circunstancias.",
    ab_p2: "En España todo avanza con citas, documentos y plazos. Un papel que falta o una fecha perdida pueden suponer meses de retraso. Por eso gran parte de nuestro trabajo es discreto y minucioso: el documento correcto, en el orden correcto, a tiempo.",
    ab_name: "¿De dónde viene el nombre? En japonés «dō» significa camino, y coincide con el apellido de nuestro fundador.",
    ab_k1_b: "Oficina en Sevilla", ab_k1_s: "Seguimiento presencial en Andalucía, no a distancia",
    ab_k2_b: "Orden documental", ab_k2_s: "Apostilla, traducción jurada MAEC y tasas oficiales",
    ab_k3_b: "Plazos reales", ab_k3_s: "Calendario alineado con Extranjería y Junta de Andalucía",
    pa_tag: "04 — Colaboración y dudas",
    pa_h2: "Para escuelas y centros",
    pa_p: "Colaboramos por escrito y con facturación oficial con academias de idiomas y centros educativos en España. Hacemos una evaluación previa de los candidatos en turco y preparamos y seguimos expedientes completos.",
    pa_list_h: "Centros colaboradores",
    pa_sh_d: "Escuela de español · Sevilla",
    faq_h2: "Preguntas frecuentes",
    q1: "No hablo español, ¿puedo empezar igualmente?", a1: "Sí. La mayoría de las rutas empiezan con un periodo en una escuela de español; te recomendamos centro y programa según tu nivel y tu objetivo.",
    q2: "¿Presentáis vosotros la solicitud de visado?", a2: "No. La presentas tú personalmente, como exige la ley. Nosotros nos encargamos de que el expediente esté completo y correcto, y de planificar citas y plazos. La decisión final corresponde a las autoridades españolas.",
    q3: "¿Cómo se determina el precio?", a3: "Según la ruta y el alcance del servicio. Te lo enviamos por escrito después de la primera consulta.",
    q4: "¿Podemos hablar mientras sigo en Turquía?", a4: "Claro. La primera consulta la hacemos por WhatsApp o videollamada; cuando llegues a Sevilla también podemos vernos en la oficina.",
    ct_tag: "05 — Contacto directo",
    ct_h2: "Cuéntanos tu objetivo y trazamos la ruta.",
    ct_p: "Escríbenos brevemente tu meta y tu calendario y te respondemos desde Sevilla. Puedes escribir en turco o en español.",
    c1: "Estudiantes", c2: "Escuelas y centros", c3: "Teléfono y WhatsApp", c4: "Oficina", c5: "Hora en Sevilla",
    row_cta: "Escríbenos sobre esta ruta",
    legal: "dogen.es es una consultoría educativa y de relocalización independiente. Las solicitudes de visado y residencia las presenta personalmente el interesado; su resolución corresponde a las autoridades españolas.",
    ind_1: "servicios", ind_2: "proceso", ind_3: "quiénes somos", ind_4: "centros y dudas"
  };

  var TR = {
    _title: document.title,
    ind_1: "hizmetler", ind_2: "süreç", ind_3: "hakkımızda", ind_4: "kurumlar ve sss"
  };
  var els = document.querySelectorAll("[data-i18n]");
  els.forEach(function (el) { TR[el.dataset.i18n] = el.textContent; });
  var DICT = { tr: TR, es: ES };
  var root = document.documentElement;
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduce) root.classList.add("d-motion");
  var lang = "tr";
  var WA = "https://wa.me/34666104496";
  var WA_MSG = {
    tr: function (s) { return "Merhaba, " + s + " hakkında bilgi almak istiyorum."; },
    es: function (s) { return "Hola, me gustaría recibir información sobre: " + s + "."; }
  };

  /* ---- Çevik Lenis Kaydırma (lerp: 0.16, duration: 0.9) ---- */
  var lenis = null;
  if (!reduce && typeof window.Lenis === "function") {
    lenis = new window.Lenis({
      duration: 0.9,
      lerp: 0.16,
      smoothWheel: true,
      smoothTouch: false,
      wheelMultiplier: 1
    });
    window.lenis = lenis;
  }

  function getFlowY(target) {
    var shell = document.querySelector("main.shell");
    if (shell) shell.classList.add("is-measuring");
    var y = window.scrollY + target.getBoundingClientRect().top;
    if (shell) shell.classList.remove("is-measuring");
    return y;
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a) return;
    var id = a.getAttribute("href").slice(1);
    if (!id || id === "top" || id === "main") {
      e.preventDefault();
      if (lenis) lenis.scrollTo(0);
      else window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
      return;
    }
    var target = document.getElementById(id);
    if (!target) return;
    e.preventDefault();
    var dest = Math.max(0, getFlowY(target) - 12);
    if (lenis) lenis.scrollTo(dest);
    else window.scrollTo({ top: dest, behavior: reduce ? "auto" : "smooth" });
  });

  /* ---- Başlık: Kelime Kelime Giriş ---- */
  function splitWords(el) {
    var text = el.textContent.trim();
    el.setAttribute("aria-label", text);
    el.classList.remove("is-in");
    el.innerHTML = text.split(/\s+/).map(function (w, i) {
      var safe = w.replace(/&/g, "&amp;").replace(/</g, "&lt;");
      return '<span class="w" aria-hidden="true"><span style="--i:' + i + '">' + safe + "</span></span>";
    }).join(" ");
    setTimeout(function () { el.classList.add("is-in"); }, 24);
  }

  /* ---- Sevilla Saati ---- */
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

  /* ---- Dil Geçişi ---- */
  var mqTrack = document.getElementById("mq-track");
  function buildMarquee(d) {
    if (!mqTrack) return;
    var words = [d.mq_1, d.mq_2, d.mq_3, d.mq_4];
    var html = "";
    for (var r = 0; r < 5; r++) {
      for (var i = 0; i < words.length; i++) html += "<span>" + words[i] + "</span>";
    }
    mqTrack.innerHTML = html;
  }

  function setLang(next) {
    var d = DICT[next] || TR;
    lang = next;
    root.lang = next;
    document.title = d._title;
    els.forEach(function (el) { var v = d[el.dataset.i18n]; if (v) el.textContent = v; });
    document.querySelectorAll(".split").forEach(splitWords);
    document.querySelectorAll(".p-row .p-us").forEach(function (c) { c.dataset.label = d.th_us; });
    document.querySelectorAll(".p-row .p-you").forEach(function (c) { c.dataset.label = d.th_you; });
    document.querySelectorAll(".row-link").forEach(function (a) {
      a.href = WA + "?text=" + encodeURIComponent(WA_MSG[next](d[a.dataset.svc]));
    });
    document.querySelectorAll(".lang button").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.lang === next));
    });
    buildMarquee(d);
    tick();
    curInd = null;
    measure();
    try { localStorage.setItem("dogen-lang", next); } catch (e) {}
  }

  document.querySelectorAll(".lang button").forEach(function (b) {
    b.addEventListener("click", function () {
      if (b.dataset.lang === lang) return;
      if (reduce) { setLang(b.dataset.lang); return; }
      root.classList.add("is-swapping");
      setTimeout(function () { setLang(b.dataset.lang); root.classList.remove("is-swapping"); }, 170);
    });
  });

  /* ---- Katmanlı Sticky Kart + Marquee + Bölüm Göstergesi Motoru ---- */
  var header = document.querySelector(".site-header");
  var bar = document.querySelector(".d-bar");
  var ind = document.querySelector(".d-ind");
  var indN = ind ? ind.querySelector("b") : null;
  var indT = ind ? ind.querySelector("span") : null;
  var cards = Array.prototype.slice.call(document.querySelectorAll("main.shell > .d-card"));
  var stack = cards.map(function (el, i) { return { el: el, nx: cards[i + 1] || null, v: -1 }; }).filter(function (s) { return s.nx; });
  var ghosts = Array.prototype.slice.call(document.querySelectorAll(".d-ghost"));
  var pRowsBox = document.querySelector(".p-rows");
  var pRows = Array.prototype.slice.call(document.querySelectorAll(".p-row"));
  var darkZones = [document.getElementById("hakkimizda"), document.getElementById("iletisim")].filter(Boolean);
  var archFig = document.querySelector(".arch-figure");
  var indDefs = [
    { id: "hizmetler", n: "01", k: "ind_1" },
    { id: "surec", n: "02", k: "ind_2" },
    { id: "hakkimizda", n: "03", k: "ind_3" },
    { id: "kurumlar", n: "04", k: "ind_4" }
  ].map(function (o) { return { el: document.getElementById(o.id), n: o.n, k: o.k }; }).filter(function (o) { return o.el; });
  var endSec = document.getElementById("iletisim");

  var vh = window.innerHeight, mqW = 0, prevY = window.scrollY, lastY = -1, vel = 0, curInd = null;
  var clamp = function (v) { return v < 0 ? 0 : v > 1 ? 1 : v; };
  var easeOut3 = function (p) { return 1 - Math.pow(1 - p, 3); };

  var cardFlows = [];
  var navLinksMap = {};
  document.querySelectorAll(".nav a").forEach(function (a) { navLinksMap[a.getAttribute("href").slice(1)] = a; });

  function measure() {
    vh = window.innerHeight;
    var shell = document.querySelector("main.shell");
    if (shell) shell.classList.add("is-measuring");
    cardFlows = cards.map(function (c) {
      return { id: c.id, el: c, top: window.scrollY + c.getBoundingClientRect().top, h: c.offsetHeight };
    });
    if (shell) shell.classList.remove("is-measuring");

    if (window.innerWidth > 560) {
      cards.forEach(function (c) {
        c.style.top = Math.min(0, vh - c.offsetHeight) + "px";
      });
    } else {
      cards.forEach(function (c) { c.style.top = ""; });
    }
    if (mqTrack) mqW = mqTrack.scrollWidth / 5;
    lastY = -1;
  }

  document.querySelectorAll(".faq details").forEach(function (d) {
    d.addEventListener("toggle", function () {
      setTimeout(measure, 40);
      setTimeout(measure, 380);
    });
  });

  function onScroll(y) {
    /* Header gizle/göster + koyu bölge algılama */
    if (!reduce && header) {
      if (y > 260 && y > prevY + 4) header.classList.add("is-hidden");
      else if (y < prevY - 3 || y < 220) header.classList.remove("is-hidden");
    }
    if (header) {
      var onDark = darkZones.some(function (sec) {
        var r = sec.getBoundingClientRect();
        return r.top <= 62 && r.bottom >= 40;
      });
      header.classList.toggle("on-dark", onDark);
    }

    /* Üst menü aktif bölüm vurgusu (flow konumuna göre, yukarı dönüşlerde de tam doğru) */
    var activeId = "";
    var probe = y + vh * 0.36;
    cardFlows.forEach(function (cf) {
      if (cf.id && cf.id !== "top" && probe >= cf.top) activeId = cf.id;
    });
    Object.keys(navLinksMap).forEach(function (k) {
      navLinksMap[k].classList.toggle("is-current", k === activeId);
    });

    /* Üst ilerleme çubuğu */
    var max = document.documentElement.scrollHeight - vh;
    if (bar) bar.style.setProperty("--sp", max > 0 ? clamp(y / max).toFixed(4) : 0);

    if (reduce) return;

    /* Hero kemer hafif paralaks */
    if (archFig && y < vh * 1.2) {
      archFig.style.setProperty("--ay", (y * -0.09).toFixed(1));
    }

    /* Arkada kalan kartın örtülme oranı (--cv) */
    if (window.innerWidth > 560) {
      stack.forEach(function (s) {
        var t = s.nx.getBoundingClientRect().top;
        var v = Math.round(easeOut3(clamp((vh * 0.72 - t) / (vh * 0.52))) * 100) / 100;
        if (v !== s.v) { s.v = v; s.el.style.setProperty("--cv", v); }
      });
    }

    /* Hayalet rakam paralaksı */
    ghosts.forEach(function (g) {
      var r = g.parentNode.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      g.style.setProperty("--gy", (Math.max(0, -r.top) * 0.32).toFixed(1));
    });

    /* Süreç satırları kaydırma odağı */
    if (pRowsBox && pRows.length) {
      var rb = pRowsBox.getBoundingClientRect();
      var inView = rb.top < vh * 0.76 && rb.bottom > vh * 0.25;
      pRowsBox.classList.toggle("is-focus", inView);
      if (inView) {
        var sr = pRowsBox.closest(".d-card").getBoundingClientRect();
        var endTop = vh - (sr.bottom - rb.bottom) - rb.height + vh * 0.08, startTop = vh * 0.68;
        var rp = startTop > endTop ? clamp((startTop - rb.top) / (startTop - endTop)) : 0;
        var best = pRows[Math.min(pRows.length - 1, Math.floor(rp * pRows.length))];
        pRows.forEach(function (row) { row.classList.toggle("is-on", row === best); });
      }
    }

    /* Sol dikey bölüm göstergesi */
    if (ind) {
      var cur = null;
      indDefs.forEach(function (n) { if (n.el.getBoundingClientRect().top <= vh * 0.52) cur = n; });
      var show = !!cur && (!endSec || endSec.getBoundingClientRect().top > vh * 0.52);
      ind.classList.toggle("show", show);
      if (show) {
        var d = DICT[lang] || TR;
        if (cur !== curInd) { curInd = cur; indN.textContent = cur.n; indT.textContent = d[cur.k] || ""; }
        var cr = cur.el.getBoundingClientRect();
        ind.style.setProperty("--ip", clamp((vh * 0.52 - cr.top) / Math.max(1, cr.height - vh * 0.4)).toFixed(3));
      }
    }
  }

  function frame(now) {
    if (lenis) lenis.raf(now);
    var y = window.scrollY;
    vel += ((y - prevY) - vel) * 0.14;
    if (y !== lastY) { onScroll(y); lastY = y; }
    prevY = y;

    if (!reduce && mqTrack && mqW > 0) {
      var skew = Math.max(-8, Math.min(8, vel * 0.22));
      var pos = y * 0.48 + now * 0.032;
      var x = -(((pos % mqW) + mqW) % mqW);
      mqTrack.style.transform = "translate3d(" + x.toFixed(1) + "px,0,0) skewX(" + (-skew).toFixed(2) + "deg)";
    }
    requestAnimationFrame(frame);
  }

  /* ---- Görünürlük Gözlemcileri (Reveal) ---- */
  if ("IntersectionObserver" in window) {
    var revObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); revObs.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -10% 0px" });
    document.querySelectorAll(".reveal, .svc-card, .p-row, .clip-h").forEach(function (el) { revObs.observe(el); });
  } else {
    document.querySelectorAll(".reveal, .svc-card, .p-row, .clip-h").forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ---- Çini Karolar: Dalga ve Dokunuşla Dönme ---- */
  (function tiles() {
    var g = document.getElementById("tiles");
    var arch = document.getElementById("arch");
    if (!g || !arch) return;
    var S = 88, COLS = 5, ROWS = 7;
    var corner = '<g fill="#f6f4ef" fill-opacity=".85"><path d="M0 0h11L0 11Z"/><path d="M88 0H77l11 11Z"/><path d="M0 88h11L0 77Z"/><path d="M88 88H77l11-11Z"/></g>';
    var star = '<g class="rot"><g transform="translate(44 44)" fill="none" stroke="#f6f4ef" stroke-width="1.6">' +
      '<rect x="-22" y="-22" width="44" height="44"/><rect x="-22" y="-22" width="44" height="44" transform="rotate(45)"/>' +
      '<circle r="9" stroke="#e2b764"/><circle class="dot" r="3.5" fill="#e2b764" stroke="none"/></g></g>';
    var list = [], html = "";
    for (var r = 0; r < ROWS; r++) for (var c = 0; c < COLS; c++) {
      html += '<g class="tile' + (reduce ? "" : " pre") + '" data-r="' + r + '" data-c="' + c + '" transform="translate(' + c * S + " " + r * S + ')">' +
        '<rect class="hit" width="88" height="88" fill="#1f4a7a"/><path d="M.5.5h87v87H.5z" fill="none" stroke="#f6f4ef" stroke-opacity=".14"/>' + corner + star + "</g>";
    }
    g.innerHTML = html;
    var fb = document.getElementById("tile-fallback"); if (fb) fb.remove();
    g.querySelectorAll(".tile").forEach(function (t) { list.push({ el: t, rot: t.querySelector(".rot"), r: +t.dataset.r, c: +t.dataset.c, a: 0, last: 0 }); });
    if (reduce) return;

    var ready = false;
    list.forEach(function (t) { setTimeout(function () { t.el.classList.remove("pre"); }, 220 + (t.r + t.c) * 65); });
    setTimeout(function () { ready = true; }, 220 + (ROWS + COLS) * 65 + 850);

    function spin(t) {
      var now = performance.now();
      if (!ready || now - t.last < 900) return;
      t.last = now; t.a += 90;
      t.rot.style.transform = "rotate(" + t.a + "deg)";
      t.el.classList.add("hot");
      setTimeout(function () { t.el.classList.remove("hot"); }, 850);
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
        setTimeout(function () { spin(t); }, d * 85);
      });
    }, 6800);
  })();

  /* ---- İlk Dil & Başlatma ---- */
  var initial = "tr";
  try {
    var q = new URLSearchParams(location.search).get("lang");
    var saved = localStorage.getItem("dogen-lang");
    if (q === "es" || q === "tr") initial = q;
    else if (saved === "es" || saved === "tr") initial = saved;
    else if (/^es\b/i.test(navigator.language || "")) initial = "es";
  } catch (e) {}
  setLang(initial);

  window.addEventListener("resize", measure, { passive: true });
  window.addEventListener("load", measure, { once: true });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);
  requestAnimationFrame(frame);

  var yr = document.getElementById("yr");
  if (yr) yr.textContent = String(new Date().getFullYear());
})();
