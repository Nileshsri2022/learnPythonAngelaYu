/*
 * Per-browser study progress.
 *
 * Day pages carry one "I have finished this day" checkbox. Ticking it stores a flag
 * in localStorage keyed by page path, and the home page widget counts how many days
 * are ticked and draws the progress bar. Nothing leaves the browser.
 */
(function () {
  "use strict";

  var PREFIX = "python100:progress:";

  function storageAvailable() {
    try {
      var k = PREFIX + "test";
      window.localStorage.setItem(k, "1");
      window.localStorage.removeItem(k);
      return true;
    } catch (err) {
      return false;
    }
  }

  function keyFor(path, index) {
    return PREFIX + path + "#" + index;
  }

  function completedDays() {
    var days = {};
    try {
      for (var i = 0; i < window.localStorage.length; i++) {
        var key = window.localStorage.key(i);
        if (!key || key.indexOf(PREFIX + "days/") !== 0) continue;
        if (window.localStorage.getItem(key) !== "1") continue;
        var m = key.match(/days\/0?(\d+)\//);
        if (m) days[m[1]] = true;
      }
    } catch (err) {
      /* storage blocked — the widget just reports zero */
    }
    return days;
  }

  function updateWidget() {
    var line = document.getElementById("progress-line");
    var fill = document.getElementById("progress-fill");
    if (!line && !fill) return;

    var widget = document.getElementById("progress-widget");
    var total = widget ? parseInt(widget.getAttribute("data-days") || "85", 10) : 85;
    var done = Object.keys(completedDays()).length;
    var percent = total ? Math.round((done / total) * 100) : 0;

    if (line) {
      line.textContent = done
        ? done + " / " + total + " days marked complete (" + percent + "%)"
        : "no days marked yet";
    }
    if (fill) fill.style.width = percent + "%";
  }

  function setupPage() {
    var container = document.querySelector(".md-content__inner") || document.body;
    var boxes = container.querySelectorAll('.task-list-item input[type="checkbox"]');
    var canStore = storageAvailable();

    Array.prototype.forEach.call(boxes, function (box, index) {
      var key = keyFor(window.location.pathname, index);
      var item = box.closest ? box.closest(".task-list-item") : null;

      if (canStore) {
        box.checked = window.localStorage.getItem(key) === "1";
      }
      box.disabled = false;
      if (item && box.checked) item.classList.add("task-list-item--done");

      box.addEventListener("change", function () {
        if (canStore) {
          window.localStorage.setItem(key, box.checked ? "1" : "0");
        }
        if (item) item.classList.toggle("task-list-item--done", box.checked);
        updateWidget();
      });
    });

    updateWidget();
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(setupPage);       // Material instant loading
  } else {
    document.addEventListener("DOMContentLoaded", setupPage);
  }
})();
