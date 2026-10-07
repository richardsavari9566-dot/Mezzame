/* Mezzame homepage interactions. Each section initialises independently so the
   theme editor can re-render one section without touching the others. */
(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const designMode = Boolean(window.Shopify && window.Shopify.designMode);

  function rotator(root, slideSelector, dotSelector) {
    const slides = [...root.querySelectorAll(slideSelector)];
    const dots = dotSelector ? [...root.querySelectorAll(dotSelector)] : [];
    let index = 0;
    const show = (n) => {
      if (!slides.length) return;
      index = (n + slides.length) % slides.length;
      slides.forEach((slide, i) => {
        const active = i === index;
        slide.classList.toggle('is-active', active);
        slide.setAttribute('aria-hidden', String(!active));
        slide.inert = !active;
      });
      dots.forEach((dot, i) => {
        dot.classList.toggle('is-active', i === index);
        dot.setAttribute('aria-current', String(i === index));
      });
    };
    root.addEventListener('shopify:block:select', (event) => {
      const i = slides.findIndex((slide) => slide === event.target || slide.contains(event.target));
      if (i >= 0) show(i);
    });
    show(0);
    return { show, next: () => show(index + 1), prev: () => show(index - 1), count: slides.length };
  }

  const initializers = {
    hero(root) {
      const r = rotator(root, '.mzh-hero__slide', '.mzh-hero__dot');
      root.querySelector('[data-mzh-next]')?.addEventListener('click', r.next);
      root.querySelector('[data-mzh-prev]')?.addEventListener('click', r.prev);
      root.querySelectorAll('.mzh-hero__dot').forEach((dot, i) => dot.addEventListener('click', () => r.show(i)));
      const delay = Number(root.dataset.autoplay || 0) * 1000;
      if (delay && r.count > 1 && !reduceMotion && !designMode) {
        let timer = setInterval(r.next, delay);
        root.addEventListener('mouseenter', () => clearInterval(timer));
        root.addEventListener('mouseleave', () => { clearInterval(timer); timer = setInterval(r.next, delay); });
        root.addEventListener('focusin', () => clearInterval(timer));
      }
    },

    gallery(root) {
      const r = rotator(root, '.mzh-gallery__slide');
      root.querySelector('[data-mzh-next]')?.addEventListener('click', r.next);
      root.querySelector('[data-mzh-prev]')?.addEventListener('click', r.prev);
    },

    tabs(root) {
      const tabs = [...root.querySelectorAll('[role="tab"]')];
      const select = (tab) => {
        tabs.forEach((t) => {
          const on = t === tab;
          t.setAttribute('aria-selected', String(on));
          t.tabIndex = on ? 0 : -1;
          const panel = root.querySelector('#' + t.getAttribute('aria-controls'));
          if (panel) panel.hidden = !on;
        });
      };
      tabs.forEach((tab, i) => {
        tab.addEventListener('click', () => select(tab));
        tab.addEventListener('keydown', (event) => {
          if (event.key !== 'ArrowRight' && event.key !== 'ArrowLeft') return;
          const next = tabs[(i + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length];
          select(next);
          next.focus();
        });
      });
      root.addEventListener('shopify:block:select', (event) => {
        const panel = event.target.closest('[role="tabpanel"]');
        const tab = panel && tabs.find((t) => t.getAttribute('aria-controls') === panel.id);
        if (tab) select(tab);
      });
    },

    pack(root) {
      const panel = root.querySelector('.mzh-film-panel');
      const toggle = root.querySelector('.mzh-film-panel__toggle');
      const video = panel?.querySelector('video');
      if (!panel || !toggle) return;
      const set = (playing) => {
        panel.classList.toggle('is-playing', playing);
        toggle.textContent = playing ? 'Ⅱ' : '▶';
        toggle.setAttribute('aria-label', playing ? toggle.dataset.labelPause : toggle.dataset.labelPlay);
        if (video) playing ? video.play().catch(() => {}) : video.pause();
      };
      set(!reduceMotion);
      toggle.addEventListener('click', () => set(!panel.classList.contains('is-playing')));
    },

    film(root) {
      const film = root.querySelector('.mzh-film');
      const play = root.querySelector('.mzh-film__play');
      const template = root.querySelector('template');
      if (!film || !play || !template) return;
      play.addEventListener('click', () => {
        film.append(template.content.cloneNode(true));
        film.classList.add('is-playing');
        const video = film.querySelector('video');
        if (video) { video.controls = true; video.play().catch(() => {}); video.focus(); }
      });
    },
  };

  function init(scope) {
    scope.querySelectorAll('[data-mzh]').forEach((root) => {
      if (root.dataset.mzhReady) return;
      root.dataset.mzhReady = 'true';
      root.dataset.mzh.split(' ').forEach((name) => initializers[name]?.(root));
    });
  }

  init(document);
  document.addEventListener('shopify:section:load', (event) => init(event.target));
})();
