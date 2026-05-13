var initPhotoSwipeFromDOM = function(gallerySelector) {

    // parse slide data (url, title, size ...) from DOM elements 
    // (children of gallerySelector)
    var parseThumbnailElements = function(el) {
        var thumbElements = el.childNodes,
            numNodes = thumbElements.length,
            items = [],
            figureEl,
            linkEl,
            size,
            item;

        for(var i = 0; i < numNodes; i++) {

            figureEl = thumbElements[i]; // <figure> element

            // include only element nodes 
            if(figureEl.nodeType !== 1) {
                continue;
            }

            linkEl = figureEl.children[0]; // <a> element

            size = linkEl.getAttribute('data-size').split('x');

            // create slide object
            item = {
                src: linkEl.getAttribute('href'),
                w: parseInt(size[0], 10),
                h: parseInt(size[1], 10)
            };



            if(figureEl.children.length > 1) {
                // <figcaption> content
                item.title = figureEl.children[1].innerHTML; 
            }

            if(linkEl.children.length > 0) {
                // <img> thumbnail element, retrieving thumbnail url
                item.msrc = linkEl.children[0].getAttribute('src');
            } 

            item.el = figureEl; // save link to element for getThumbBoundsFn
            items.push(item);
        }

        return items;
    };

    // find nearest parent element
    var closest = function closest(el, fn) {
        return el && ( fn(el) ? el : closest(el.parentNode, fn) );
    };

    // triggers when user clicks on thumbnail
    var onThumbnailsClick = function(e) {
        e = e || window.event;
        e.preventDefault ? e.preventDefault() : e.returnValue = false;

        var eTarget = e.target || e.srcElement;

        // find root element of slide
        var clickedListItem = closest(eTarget, function(el) {
            return (el.tagName && el.tagName.toUpperCase() === 'FIGURE');
        });

        if(!clickedListItem) {
            return;
        }

        // find index of clicked item by looping through all child nodes
        // alternatively, you may define index via data- attribute
        var clickedGallery = clickedListItem.parentNode,
            childNodes = clickedListItem.parentNode.childNodes,
            numChildNodes = childNodes.length,
            nodeIndex = 0,
            index;

        for (var i = 0; i < numChildNodes; i++) {
            if(childNodes[i].nodeType !== 1) { 
                continue; 
            }

            if(childNodes[i] === clickedListItem) {
                index = nodeIndex;
                break;
            }
            nodeIndex++;
        }



        if(index >= 0) {
            // open PhotoSwipe if valid index found
            openPhotoSwipe( index, clickedGallery );
        }
        return false;
    };

    // parse picture index and gallery index from URL (#&pid=1&gid=2)
    var photoswipeParseHash = function() {
        var hash = window.location.hash.substring(1),
        params = {};

        if(hash.length < 5) {
            return params;
        }

        var vars = hash.split('&');
        for (var i = 0; i < vars.length; i++) {
            if(!vars[i]) {
                continue;
            }
            var pair = vars[i].split('=');  
            if(pair.length < 2) {
                continue;
            }           
            params[pair[0]] = pair[1];
        }

        if(params.gid) {
            params.gid = parseInt(params.gid, 10);
        }

        return params;
    };

    var openPhotoSwipe = function(index, galleryElement, disableAnimation, fromURL) {
        var pswpElement = document.querySelectorAll('.pswp')[0],
            gallery,
            options,
            items;

        items = parseThumbnailElements(galleryElement);

        // define options (if needed)
        options = {

            // define gallery index (for URL)
            galleryUID: galleryElement.getAttribute('data-pswp-uid'),

            getThumbBoundsFn: function(index) {
                // See Options -> getThumbBoundsFn section of documentation for more info
                var thumbnail = items[index].el.getElementsByTagName('img')[0], // find thumbnail
                    pageYScroll = window.pageYOffset || document.documentElement.scrollTop,
                    rect = thumbnail.getBoundingClientRect(); 

                return {x:rect.left, y:rect.top + pageYScroll, w:rect.width};
            }

        };

        // PhotoSwipe opened from URL
        if(fromURL) {
            if(options.galleryPIDs) {
                // parse real index when custom PIDs are used 
                // http://photoswipe.com/documentation/faq.html#custom-pid-in-url
                for(var j = 0; j < items.length; j++) {
                    if(items[j].pid == index) {
                        options.index = j;
                        break;
                    }
                }
            } else {
                // in URL indexes start from 1
                options.index = parseInt(index, 10) - 1;
            }
        } else {
            options.index = parseInt(index, 10);
        }

        // exit if index not found
        if( isNaN(options.index) ) {
            return;
        }

        if(disableAnimation) {
            options.showAnimationDuration = 0;
        }

        // Pass data to PhotoSwipe and initialize it
        gallery = new PhotoSwipe( pswpElement, PhotoSwipeUI_Default, items, options);
        gallery.init();
    };

    // loop through all gallery elements and bind events
    var galleryElements = document.querySelectorAll( gallerySelector );

    for(var i = 0, l = galleryElements.length; i < l; i++) {
        galleryElements[i].setAttribute('data-pswp-uid', i+1);
        galleryElements[i].onclick = onThumbnailsClick;
    }

    // Parse URL and open gallery if it contains #&pid=3&gid=1
    var hashData = photoswipeParseHash();
    if(hashData.pid && hashData.gid) {
        openPhotoSwipe( hashData.pid ,  galleryElements[ hashData.gid - 1 ], true, true );
    }
};

// execute above function
initPhotoSwipeFromDOM('.gl-lightbox');


.md-breadcrumb {
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.md-breadcrumb a {
  text-decoration: none;
  color: #3f51b5;
}

.md-breadcrumb a:hover {
  text-decoration: underline;
}

<<<<<<< HEAD
document.addEventListener("DOMContentLoaded", function () {
  if (document.body.classList.contains("no-zoom")) {

    document.querySelectorAll(".md-content img").forEach(img => {
      img.style.pointerEvents = "none";
      img.onclick = null;
    });

  }
});

nav li > ul {
    transition: all 0.3s ease;
    overflow: hidden;
}
=======
/* ===== Mobile Footer Auto Hide (Material for MkDocs) ===== */

function initMobileFooterHide() {

  const footer = document.querySelector(".md-footer");
  const main = document.querySelector(".md-main"); // MkDocs 的滚动容器

  if (!footer || !main) return;

  let lastScrollTop = 0;

  footer.classList.add("show");

  main.addEventListener("scroll", function () {

    if (window.innerWidth > 768) return;

    let st = main.scrollTop;

    if (st > lastScrollTop) {
      // 向下滚动
      footer.classList.remove("show");
      footer.classList.add("hide");
    } else {
      // 向上滚动
      footer.classList.remove("hide");
      footer.classList.add("show");
    }

    lastScrollTop = st <= 0 ? 0 : st;

  });

}
document.addEventListener("DOMContentLoaded", function() {
  const footer = document.querySelector(".md-footer");
  const main = document.querySelector(".md-main"); // Material 的滚动容器

  if (!footer || !main) return;

  let lastScrollTop = 0;
  const delta = 5;

  // 初始显示
  footer.classList.add("show");

  main.addEventListener("scroll", function () {
    if (window.innerWidth > 768) return;

    let st = main.scrollTop;

    if (Math.abs(st - lastScrollTop) <= delta) return;

    if (st > lastScrollTop) {
      // 向下滚动 → 隐藏
      footer.classList.remove("show");
      footer.classList.add("hide");
    } else {
      // 向上滚动 → 显示
      footer.classList.remove("hide");
      footer.classList.add("show");
    }

    lastScrollTop = st <= 0 ? 0 : st;
  });
});
>>>>>>> 17d334a88abb8b948994d7245df47e8074cd4c5f

document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelector(".md-tabs");
    if (!tabs) return;

    let lastScrollTop = 0;

    window.addEventListener("scroll", function () {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

        if (currentScroll > lastScrollTop && currentScroll > 80) {
            // 向下滚动 → 隐藏
            tabs.classList.add("md-tabs--hidden");
        } else {
            // 向上滚动 → 显示
            tabs.classList.remove("md-tabs--hidden");
        }

        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
    });
});

document.addEventListener("DOMContentLoaded", function () {

    const tabs = document.querySelector(".md-tabs");

    if (!tabs) {
        console.log("md-tabs not found");
        return;
    }

    let lastScroll = window.scrollY;

    window.addEventListener("scroll", function () {

        const currentScroll = window.scrollY;

        // 向下滚动并且超过 100px
        if (currentScroll > lastScroll && currentScroll > 100) {
            tabs.classList.add("hidden");
        }

        // 向上滚动
        else {
            tabs.classList.remove("hidden");
        }

        lastScroll = currentScroll;
    });

});