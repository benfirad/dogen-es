/* dogen.es — dil değiştirici, başlık gölgesi, görünme animasyonu.
   Türkçe metinler HTML'den okunur; burada yalnızca İspanyolca karşılıklar durur. */
(function () {
  "use strict";

  var ES = {
    _title: "dogen.es — Consultoría educativa y de relocalización en España",
    skip: "Saltar al contenido",
    nav_services: "Servicios", nav_process: "Proceso", nav_partners: "Centros", nav_faq: "FAQ", nav_contact: "Contacto",
    hero_eyebrow: "Consultoría educativa desde Sevilla",
    hero_h1: "Estudiar en España empieza por el <em>camino correcto</em>.",
    hero_lead: "De la escuela de español a la Formación Profesional, de la universidad al expediente de visado y los primeros 30 días en España: construimos el proceso contigo, paso a paso, desde Sevilla.",
    cta_primary: "Reservar una primera consulta",
    cta_secondary: "Ver servicios",
    meta_1: "Oficina presencial en Sevilla", meta_2: "Turco y español", meta_3: "De la solicitud a los primeros 30 días",
    route_k: "Tu ruta", route_from: "Estambul",
    route_p: "En una breve consulta aclaramos tu objetivo, presupuesto y calendario, y te entregamos por escrito el camino que mejor encaja contigo.",
    svc_eyebrow: "Servicios", svc_h2: "Cuatro caminos, un solo plan.",
    svc_p: "Elijas la ruta que elijas, coordinamos centro, documentación y llegada en un único calendario.",
    s1_t: "Escuela de español", s1_d: "Programas intensivos de español en centros acreditados por el Instituto Cervantes.",
    s1_a: "Elección de centro según nivel", s1_b: "Programa válido para visado de estudios", s1_c: "Orientación de alojamiento",
    s2_t: "Formación Profesional (FP)", s2_d: "Ciclos de Grado Superior gratuitos en centros públicos españoles.",
    s2_a: "Elección de ciclo y centro", s2_b: "Homologación de títulos", s2_c: "Calendario de admisión",
    s3_t: "Universidad", s3_d: "Acreditación UNEDasiss y preinscripción en universidades públicas andaluzas vía DUA.",
    s3_a: "Registro en UNEDasiss", s3_b: "Preinscripción DUA", s3_c: "Estrategia de grados y preferencias",
    s4_t: "Llegada y asentamiento", s4_d: "Organizamos contigo la burocracia de tus primeras semanas en España.",
    s4_a: "Empadronamiento", s4_b: "Certificado digital", s4_c: "Cita de NIE / TIE",
    proc_eyebrow: "Proceso", proc_h2: "Del primer mensaje a tu primer mes en España.",
    proc_p: "En cada paso sabes desde el principio qué se hace, quién lo hace y cuándo.",
    p1_t: "Primera consulta", p1_d: "Tu objetivo, presupuesto, calendario y documentos actuales.",
    p2_t: "Plan de ruta", p2_d: "Escuela de español, FP o universidad: tu camino y un plan por escrito.",
    p3_t: "Admisión y documentos", p3_d: "Matrícula, traducción jurada, apostilla y homologación.",
    p4_t: "Expediente de visado", p4_d: "Orden documental consular y calendario de citas.",
    p5_t: "Llegada y primeros 30 días", p5_d: "Alojamiento, empadronamiento, certificado digital, NIE/TIE.",
    ap_eyebrow: "Nuestro enfoque", ap_h2: "Pocas palabras, expedientes completos.",
    ap_p: "En lugar de paquetes cerrados y grandes promesas, una forma de trabajar tranquila y rigurosa que mira con realismo cada caso.",
    ap_name: "<strong>¿Por qué «dogen»?</strong> En japonés, <strong>dō</strong> significa «camino». Unida al apellido de nuestro fundador, Fırat Daşdöğen, esta palabra resume nuestro trabajo: acompañarte por el camino correcto, paso a paso.",
    pr1_t: "Un punto de partida realista", pr1_d: "Analizamos tu perfil desde cero y con honestidad, sin plantillas.",
    pr2_t: "Expedientes completos", pr2_d: "Rigor total en traducciones, apostillas, homologaciones y documentación consular.",
    pr3_t: "Calendario anticipado", pr3_d: "Planificamos matrícula, visado y residencia con meses de antelación.",
    pa_eyebrow: "Para escuelas y centros", pa_h2: "Conecta con el candidato adecuado desde Turquía, con un proceso transparente.",
    pa_p: "Colaboramos de forma formal y por escrito con academias de idiomas y centros educativos en España.",
    pa_cta: "Escríbenos para colaborar",
    pa_1: "Evaluación previa de candidatos en turco", pa_2: "Expedientes completos y con seguimiento", pa_3: "Colaboración formal con facturación oficial",
    faq_eyebrow: "Preguntas frecuentes", faq_h2: "Lo que te preguntas.",
    q1: "No hablo español, ¿puedo empezar igualmente?", a1: "Sí. La mayoría de las rutas empiezan con un periodo en una escuela de español; te recomendamos centro y programa según tu nivel y objetivo.",
    q2: "¿Presentáis vosotros la solicitud de visado?", a2: "No. La solicitud la presentas tú personalmente, como exige la ley. Nosotros nos encargamos de que el expediente esté completo y correcto, y de planificar citas y plazos. La decisión final corresponde a las autoridades españolas.",
    q3: "¿Cómo se determina el precio?", a3: "El precio depende de la ruta y del alcance del servicio, y se comparte por escrito tras la primera consulta.",
    q4: "¿Podemos hablar mientras sigo en Turquía?", a4: "Por supuesto. Las primeras consultas se hacen por WhatsApp o videollamada; cuando llegues a Sevilla, también podemos vernos en nuestra oficina.",
    ct_eyebrow: "Contacto", ct_h2: "Tracemos tu ruta juntos.",
    ct_p: "Empieza con un mensaje breve: cuéntanos tu objetivo, tu calendario y tus dudas. Puedes escribir en turco o en español.",
    ct_wa: "Escríbenos por WhatsApp", ct_mail: "Enviar un correo",
    c1: "Estudiantes y candidatos", c2: "Escuelas y alianzas", c3: "Teléfono / WhatsApp", c4: "Oficina",
    legal: "dogen.es ofrece consultoría educativa y de relocalización independiente; las solicitudes de visado y extranjería las presenta personalmente el interesado y su resolución compete a las autoridades españolas."
  };

  var TR = { _title: document.title };
  var textEls = document.querySelectorAll("[data-i18n]");
  var htmlEls = document.querySelectorAll("[data-i18n-html]");
  textEls.forEach(function (el) { TR[el.dataset.i18n] = el.textContent; });
  htmlEls.forEach(function (el) { TR[el.dataset.i18nHtml] = el.innerHTML; });
  var DICT = { tr: TR, es: ES };

  function setLang(lang) {
    var d = DICT[lang] || TR;
    document.documentElement.lang = lang;
    document.title = d._title;
    textEls.forEach(function (el) { var v = d[el.dataset.i18n]; if (v) el.textContent = v; });
    htmlEls.forEach(function (el) { var v = d[el.dataset.i18nHtml]; if (v) el.innerHTML = v; });
    document.querySelectorAll(".lang button").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.lang === lang));
    });
    try { localStorage.setItem("dogen-lang", lang); } catch (e) {}
  }

  document.querySelectorAll(".lang button").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.dataset.lang); });
  });

  // İlk dil: ?lang= > kayıtlı tercih > tarayıcı dili
  var initial = "tr";
  try {
    var q = new URLSearchParams(location.search).get("lang");
    var saved = localStorage.getItem("dogen-lang");
    if (q === "es" || q === "tr") initial = q;
    else if (saved === "es" || saved === "tr") initial = saved;
    else if (/^es\b/i.test(navigator.language || "")) initial = "es";
  } catch (e) {}
  if (initial !== "tr") setLang(initial);

  // Başlık alt çizgisi
  var header = document.querySelector(".site-header");
  var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Görünme animasyonu
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("is-in"); });
  }

  var yr = document.getElementById("yr");
  if (yr) yr.textContent = String(new Date().getFullYear());
})();
