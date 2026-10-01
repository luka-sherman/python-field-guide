(function () {
  // mermaid.initialize() is mermaid's own real configuration API — a
  // different mechanism than a `%%{init: ...}%%` directive written inside
  // a diagram's own source, which is silently ignored by this site's
  // mermaid setup (verified directly: setting a bright, unmistakable color
  // through one had no effect at all). A real initialize() call configures
  // the renderer itself, so unlike any CSS or DOM patch attempted after
  // the fact, it isn't blocked by a diagram's closed shadow root — there's
  // nothing to reach into yet when this runs.
  //
  // A single initialize() call here, before Material's own render trigger,
  // had no visible effect — Material calls mermaid.initialize() itself
  // when it actually renders, and that call almost certainly replaces the
  // `flowchart` config object wholesale rather than merging into whatever
  // was set before it, wiping these overrides out before they're ever
  // used. Wrapping initialize() instead means these overrides get folded
  // into *every* call, including Material's own, regardless of call order
  // or how many times it's called.
  //
  // Can't make a diagram literally fill its container: mermaid's
  // useMaxWidth setting only ever shrinks an oversized diagram down to fit
  // a narrow viewport, it never stretches an undersized one to fill a wide
  // one. The actual levers for "wider" are the diagram's own authored
  // layout — nodeSpacing is the horizontal gap between the two lanes;
  // wrappingWidth is how wide a node's own text gets before it wraps,
  // which is what actually determines each node box's width (confirmed in
  // the rendered SVG: each label's foreignObject carries an inline
  // `max-width: 200px`, mermaid's wrappingWidth default).
  if (!window.mermaid) return;

  const originalInitialize = window.mermaid.initialize.bind(window.mermaid);

  window.mermaid.initialize = function (config) {
    config = config || {};
    config.flowchart = Object.assign({}, config.flowchart, {
      nodeSpacing: 150,
      wrappingWidth: 400,
    });
    return originalInitialize(config);
  };
})();
