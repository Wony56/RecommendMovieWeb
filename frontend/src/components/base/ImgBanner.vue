<template>

  <section class="slider-pages">
  <article class="js-scrolling__page js-scrolling__page-1 js-scrolling--active">
    
    <div class="slider-page slider-page--left">
      
      <div class="slider-page--skew">
        
        <div class="slider-page__content">
          <vue-particles
            color="#fff"
            :particleOpacity="0.9"
            :particlesNumber="100"
            shapeType="circle"
            :particleSize="6"
            linesColor="#fff"
            :linesWidth="1"
            :lineLinked="true"
            :lineOpacity="0.9"
            :linesDistance="150"
            :moveSpeed="5"
            :hoverEffect="true"
            hoverMode="grab"
            :clickEffect="true"
            clickMode="push"
          >
          </vue-particles>
        </div>
        
        <!-- /.slider-page__content -->
      </div>
      
      <!-- /.slider-page--skew -->
    </div>
    
    <!-- /.slider-page slider-page--left -->
      
    <div class="slider-page slider-page--right">
      <div class="slider-page--skew">
        
        <div class="slider-page__content">
          
          
          <h1 class="slider-page__title slider-page__title--big" style="color:#ff2f6e">
            Dunkerque
          </h1>
          <!-- /.slider-page__title -->
          <p class="slider-page__description">
           Christopher Edward Nolan
          </p>
          <!-- /.slider-page__description -->
         
        </div>
        <!-- /.slider-page__content -->
        
      </div>
      <!-- /.slider-page--skew -->
    </div>
    <!-- /.slider-page slider-page--right -->
     
  </article>
  <!-- /.js-scrolling__page js-scrolling__page-1 js-scrolling--active -->


  <article class="js-scrolling__page js-scrolling__page-2">
    <div class="slider-page slider-page--left">
      <div class="slider-page--skew">
        <div class="slider-page__content">
          <h1 class="slider-page__title" style="color:#ff2f6e">
            Avengers - End Game
          </h1>
          <!-- /.slider-page__title -->
          <p class="slider-page__description">
            Mavel Studio
          </p>
          <!-- /.slider-page__description -->
        </div>
        <!-- /.slider-page__content -->
      </div>
      <!-- /.slider-page--skew -->
    </div>
    <!-- /.slider-page slider-page--left -->

    <div class="slider-page slider-page--right">
      <div class="slider-page--skew">
        <div class="slider-page__content">
          <vue-particles
            color="#fff"
            :particleOpacity="0.9"
            :particlesNumber="100"
            shapeType="circle"
            :particleSize="6"
            linesColor="#fff"
            :linesWidth="1"
            :lineLinked="true"
            :lineOpacity="0.9"
            :linesDistance="150"
            :moveSpeed="5"
            :hoverEffect="true"
            hoverMode="grab"
            :clickEffect="true"
            clickMode="push"
          >
          </vue-particles>
        </div>
        <!-- /.slider-page__content -->
      </div>
      <!-- /.slider-page--skew -->
    </div>
    <!-- /.slider-page slider-page--right -->
  </article>
  <!-- /.js-scrolling__page js-scrolling__page-2 -->

  <article class="js-scrolling__page js-scrolling__page-3">
    <div class="slider-page slider-page--left">
      <div class="slider-page--skew">
        <div class="slider-page__content">
          <vue-particles
            color="#fff"
            :particleOpacity="0.9"
            :particlesNumber="80"
            shapeType="circle"
            :particleSize="6"
            linesColor="#fff"
            :linesWidth="1"
            :lineLinked="true"
            :lineOpacity="0.9"
            :linesDistance="150"
            :moveSpeed="5"
            :hoverEffect="true"
            hoverMode="grab"
            :clickEffect="true"
            clickMode="push"
          >
          </vue-particles>
        </div>
        <!-- /.slider-page__content -->
      </div>
      <!-- /.slider-page--skew -->
    </div>
    <!-- /.slider-page slider-page--left -->

    <div class="slider-page slider-page--right">
      <div class="slider-page--skew">
        <div class="slider-page__content">
          <h1 class="slider-page__title" style="color:#ff2f6e">
            Jig Saw
          </h1>
          <!-- /.slider-page__title -->
          <p class="slider-page__description">
            Michael Spierig
          </p>
          <!-- /.slider-page__description -->
        </div>
        <!-- /.slider-page__content -->
      </div>
      <!-- /.slider-page--skew -->
    </div>
    <!-- /.slider-page slider-page--right -->
  </article>
  <!-- /.js-scrolling__page js-scrolling__page-3 -->
</vue-particles>
</section>
<!-- /.slider-pages -->

</template>

<style lang="scss">
/***********************
 *	Variables
 **********************/
$font-family:             'Open Sans', sans-serif;
$font-size:               1em;

$color-body:              #282828;
$color-text:              #e2e2e2;
$color-link:              #80a1c1;
$color-link-active:       #6386a9;

$variable-skewX:          18deg;
$variable-vHForSkewX:     32.5vh;
$variable-scrollingTime:  1350ms;

/***********************
 *	Project Main Styles
 **********************/
*,
*:before,
*:after {
  box-sizing: border-box;
  margin:     0;
  padding:    0;
}

body {
  font-family:      $font-family;
  background-color: $color-body;
}

.slider-pages {
  overflow: hidden;
  position: relative;

  height:   86vh;
}

.slider-page {
  position:   absolute;

  top:        0;
  width:      50%;
  height:     100vh;

  transition: transform $variable-scrollingTime;
}

.slider-page--skew {
  overflow:   hidden;
  position:   absolute;

  top:        0;
  width:      140%;
  height:     100%;

  background: $color-body;

  transform:  skewX($variable-skewX * -1);
}

.slider-page--left {
  left:       0;

  transform:  translateX($variable-vHForSkewX * -1)
              translateY(100%)
              translateZ(0);

  .slider-page--skew {
    left:     -40%;
  }

  .slider-page__content {
    padding:          auto 30% auto 30%;

    transform-origin: 100% 0;
  }
}

.slider-page--right {
  left:       50%;

  transform:  translateX($variable-vHForSkewX)
              translateY(-100%)
              translateZ(0);

  .slider-page--skew {
    right:    -40%;
  }

  .slider-page__content {
    padding:          auto 30% auto 30%;

    transform-origin: 0 100%;
  }
}

.slider-page__content {
  position:         absolute;

  display:          flex;
  justify-content:  center;
  align-items:      center;
  flex-flow:        column wrap;

  top:      0;
  left:     0;
  width:    100%;
  height:   100%;
  padding:  0 30% 0 30%;

  color:            $color-text;
  background-size:  cover;

  transform:  skewX($variable-skewX);
  transition: transform $variable-scrollingTime;
}

.slider-page__title {
  margin-bottom: 1em;

  font-size:  $font-size;
  text-align: center;

  text-transform: uppercase;
}

.slider-page__title--big {
  font-size:  $font-size * 1.2;
}

.slider-page__description {
  font-size:  $font-size;
  text-align: center;
}

.slider-page__link {
  color:      $color-link;

  &:hover,
  &:focus {
    color:            $color-link-active;
    text-decoration:  none;
  }
}

/***********************
 *	Project JS Styles
 **********************/
.js-scrolling__page {
  position:   absolute;

  top:        0;
  left:       0;
  width:      100%;
}

.js-scrolling--active {

  .slider-page {
    transform:  translateX(0)
                translateY(0)
                translateZ(0);
  }
}

.js-scrolling--inactive {

  .slider-page__content {
    transform:  skewX($variable-skewX)
                scale(.9);
  }
}

.js-scrolling__page-1 {

  .slider-page--left .slider-page__content {
    background-image: url("../../../public/img/background1.jpg");
  }

  .slider-page--right .slider-page__content {
    background-color: $color-body;
  }
}

.js-scrolling__page-2 {

  .slider-page--left .slider-page__content {
    background-color: #000;
  }
  .slider-page--left .slider-page__title,
  .slider-page--left .slider-page__description {
    color:           #fff;
  }

  .slider-page--right .slider-page__content {
    background-image: url("../../../public/img/background2.jpg");
  }
}

.js-scrolling__page-3 {

  .slider-page--left .slider-page__content {
    background-image: url("../../../public/img/background3.jpg");
  }

  .slider-page--right .slider-page__content {
    background-color: $color-body;
  }
}

</style>
<script>
export default {
  
}
/*********************
 *	Helpers Code
 ********************/
/**
                        *  @function   DOMReady
                        *
                        *  @param callback
                        *  @param element
                        *  @param listener
                        *  @returns {*}
                        *  @constructor
                        */
const DOMReady = (
callback = () => {},
element = document,
listener = 'addEventListener') =>
{
  return element[listener] ? element[listener]('DOMContentLoaded', callback) : window.attachEvent('onload', callback);
};

/**
    *  @function   ProjectAPI
    *
    *  @type {{hasClass, addClass, removeClass}}
    */
const ProjectAPI = (() => {
  let hasClass,
  addClass,
  removeClass;

  hasClass = (el, className) => {
    if (el === null) {
      return;
    }

    if (el.classList) {
      return el.classList.contains(className);
    } else
    {
      return !!el.className.match(new RegExp('(\\s|^)' + className + '(\\s|$)'));
    }
  };

  addClass = (el, className) => {
    if (el === null) {
      return;
    }

    if (el.classList) {
      el.classList.add(className);
    } else
    if (!hasClass(el, className)) {
      el.className += ' ' + className;
    }
  };

  removeClass = (el, className) => {
    if (el === null) {
      return;
    }

    if (el.classList) {
      el.classList.remove(className);
    } else
    if (hasClass(el, className)) {
      let reg = new RegExp('(\\s|^)' + className + '(\\s|$)');

      el.className = el.className.replace(reg, ' ');
    }
  };

  return {
    hasClass: hasClass,
    addClass: addClass,
    removeClass: removeClass };

})();


/*********************
       *	Application Code
       ********************/
/**
                              *  @function   readyFunction
                              *
                              *  @type {Function}
                              */
const readyFunction = () => {

  const KEY_UP = 38;
  const KEY_DOWN = 40;

  let scrollingClass = 'js-scrolling',
  scrollingActiveClass = scrollingClass + '--active',
  scrollingInactiveClass = scrollingClass + '--inactive',

  scrollingTime = 1350,
  scrollingIsActive = false,

  currentPage = 1,
  countOfPages = document.querySelectorAll('.' + scrollingClass + '__page').length,

  prefixPage = '.' + scrollingClass + '__page-',

  _switchPages,
  _scrollingUp,
  _scrollingDown,

  _mouseWheelEvent,
  _keyDownEvent,

  init;

  /**
         *  @function _switchPages
         *
         *  @private
         */
  _switchPages = () => {

    let _getPageDomEl;

    /**
                         *  @function _getPageDomEl
                         *
                         *  @param page
                         *  @returns {Element}
                         *  @private
                        */
    _getPageDomEl = (page = currentPage) => {
      return document.querySelector(prefixPage + page);
    };

    scrollingIsActive = true;


    ProjectAPI.removeClass(
    _getPageDomEl(),
    scrollingInactiveClass);

    ProjectAPI.addClass(
    _getPageDomEl(),
    scrollingActiveClass);


    ProjectAPI.addClass(
    _getPageDomEl(currentPage - 1),
    scrollingInactiveClass);


    ProjectAPI.removeClass(
    _getPageDomEl(currentPage + 1),
    scrollingActiveClass);



    setTimeout(
    () => {
      return scrollingIsActive = false;
    },
    scrollingTime);

  };
  /**
       *  @function _scrollingUp
       *
       *  @private
       */
  _scrollingUp = () => {
    if (currentPage === 1) {
      return;
    }

    currentPage--;

    _switchPages();
  };
  /**
       *  @function _scrollingDown
       *
       *  @private
       */
  _scrollingDown = () => {
    if (currentPage === countOfPages) {
      return;
    }

    currentPage++;

    _switchPages();
  };
  /**
       *  @function _mouseWheelEvent
       *
       *  @param e
       *  @private
       */
  _mouseWheelEvent = e => {
    if (scrollingIsActive) {
      return;
    }

    if (e.wheelDelta > 0 || e.detail < 0) {
      _scrollingUp();
    } else
    if (e.wheelDelta < 0 || e.detail > 0) {
      _scrollingDown();
    }
  };
  /**
       *  @function _keyDownEvent
       *
       *  @param e
       *  @private
       */
  _keyDownEvent = e => {
    if (scrollingIsActive) {
      return;
    }

    let keyCode = e.keyCode || e.which;

    if (keyCode === KEY_UP) {
      _scrollingUp();
    } else
    if (keyCode === KEY_DOWN) {
      _scrollingDown();
    }
  };

  /**
      *  @function init
      *
      *  @note     auto-launch
      */
  init = (() => {
    document.addEventListener(
    'mousewheel',
    _mouseWheelEvent,
    false);

    document.addEventListener(
    'DOMMouseScroll',
    _mouseWheelEvent,
    false);


    document.addEventListener(
    'keydown',
    _keyDownEvent,
    false);

  })();

};


/**
    *  Launcher
    */
DOMReady(readyFunction);
</script>