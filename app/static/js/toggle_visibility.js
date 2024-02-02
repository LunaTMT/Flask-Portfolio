function toggleContainerVisibility(containerId, parentContainerId=NaN) {
  var containers = document.querySelectorAll('.description-container, .overview-container, .video-container, .devlog-container, .tutorial-container, .about-container, .skills-container, .PL-container, .interests-container, .languages-container');

  containers.forEach(function(container) {
      if (container.id === containerId) {
          container.classList.toggle('hide');
      } else if (parentContainerId && container.id === parentContainerId) {
          // Skip hiding the parent container
      } else {
          container.classList.add('hide');
      }
  });
}