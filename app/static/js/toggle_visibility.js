function toggleContainerVisibility(containerId) {
    var containers = document.querySelectorAll('.description-container, .overview-container, .video-container, .devlog-container, .tutorial-container');

    containers.forEach(function(container) {
      if (container.id === containerId) {
        container.classList.toggle('hide');
      } else {
        container.classList.add('hide');
      }
    });
  }