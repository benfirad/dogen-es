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
    c1: "Estudiantes", c2: "Escuelas y centros", c3: "Teléfono y WhatsApp", c4: "Oficina",
    legal: "dogen.es es una consultoría educativa y de relocalización independiente. Las solicitudes de visado y residencia las presenta personalmente el interesado; su resolución corresponde a las autoridades españolas."
  };

  var TR = { _title: document.title };
  var els = document.querySelectorAll("[data-i18n]");
  els.forEach(function (el) { TR[el.dataset.i18n] = el.textContent; });
  var DICT = { tr: TR, es: ES };

  function setLang(lang) {
    var d = DICT[lang] || TR;
    document.documentElement.lang = lang;
    document.title = d._title;
    els.forEach(function (el) { var v = d[el.dataset.i18n]; if (v) el.textContent = v; });
    // Mobil tablo etiketleri
    document.querySelectorAll(".steps td:nth-child(2)").forEach(function (td) { td.dataset.label = d.th_us; });
    document.querySelectorAll(".steps td:nth-child(3)").forEach(function (td) { td.dataset.label = d.th_you; });
    document.querySelectorAll(".lang button").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.lang === lang));
    });
    try { localStorage.setItem("dogen-lang", lang); } catch (e) {}
  }

  document.querySelectorAll(".lang button").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.dataset.lang); });
  });

  var initial = "tr";
  try {
    var q = new URLSearchParams(location.search).get("lang");
    var saved = localStorage.getItem("dogen-lang");
    if (q === "es" || q === "tr") initial = q;
    else if (saved === "es" || saved === "tr") initial = saved;
    else if (/^es\b/i.test(navigator.language || "")) initial = "es";
  } catch (e) {}
  if (initial !== "tr") setLang(initial);

  var yr = document.getElementById("yr");
  if (yr) yr.textContent = String(new Date().getFullYear());
})();
