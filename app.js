const I18N = {
  tr: {
    title: "dogen.es — Yakında Hizmetinizdeyiz",
    status_text: "Yeni web sitemiz hazırlanıyor — Yakında hizmetinizdeyiz",
    headline: "Türkiye'den İspanya'ya eğitim, dil okulu ve yerleşim danışmanlığı.",
    lead: "Sevilla merkezli yapımızla akredite dil okulları, üniversite başvuruları, vize dosya hazırlığı ve İspanya'ya varış süreçlerinde öğrencilerimize ve kurumsal okul partnerlerimize doğrudan destek veriyoruz. Web sitemiz yayına hazırlanırken aşağıdaki kanallardan bize doğrudan ulaşabilirsiniz.",
    focus_1: "Akredite Dil Okulları & Üniversite Kabulü",
    focus_2: "Vize Hazırlığı & İlk 30 Gün Varış Desteği",
    focus_3: "İspanya'daki Eğitim Kurumları ile Resmi Faturalı Partnerlik",
    lbl_student: "Öğrenci & Danışmanlık",
    lbl_partner: "Okul & Kurumsal İş Birliği",
    lbl_phone: "Doğrudan Hat / WhatsApp"
  },
  es: {
    title: "dogen.es — Muy pronto",
    status_text: "Nuestra nueva web está en preparación — Muy pronto",
    headline: "Consultoría educativa y de relocalización entre Turquía y España.",
    lead: "Desde nuestra base en Sevilla acompañamos a estudiantes de Turquía y colaboramos con centros educativos acreditados en España en todo el proceso: matrícula en escuelas de idiomas, acceso universitario, preparación documental para visado y llegada a destino. Mientras preparamos nuestra nueva web, puedes escribirnos directamente por los siguientes canales.",
    focus_1: "Escuelas de Español Acreditadas y Acceso Universitario",
    focus_2: "Preparación de Visado y Acompañamiento Inicial (30 días)",
    focus_3: "Alianzas Corporativas con Centros en España y Facturación Oficial",
    lbl_student: "Estudiantes y Consultoría",
    lbl_partner: "Escuelas y Alianzas",
    lbl_phone: "Contacto Directo / WhatsApp"
  }
};

document.querySelectorAll(".lang-btn").forEach((btn) => {
  btn.addEventListener("click", () => {
    const lang = btn.dataset.lang;
    const dict = I18N[lang];
    if (!dict) return;
    document.documentElement.lang = lang;
    document.title = dict.title;
    document.querySelectorAll(".lang-btn").forEach((b) => b.classList.toggle("is-active", b === btn));
    document.querySelectorAll("[data-i18n]").forEach((el) => {
      const key = el.dataset.i18n;
      if (dict[key]) {
        el.textContent = dict[key];
      }
    });
  });
});
