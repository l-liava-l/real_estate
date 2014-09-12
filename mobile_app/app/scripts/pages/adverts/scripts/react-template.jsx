/** @jsx React.DOM */

React.initializeTouchEvents(false);

window.AdvertList = React.createClass({
  displayName: "AdvertList",

  componentWillMount : function() {
      var scope = this.props.scope;
      scope.advertList.react = this;
      scope.$digest();
      scope.loadMore();
  },

  render: function() {

      var scope = this.props.scope;
      var items = scope.visible.map(function(advert, index, array) {

        advert.slider = 'slider' + index;

        var images = advert.images.map(function(img) {
            return (
             <div className="slide">
                <img className="full-image" src={img}></img>
            </div>)
        });

        var numbers = advert.numbers.map(function(num) {
            return (<a>{num} </a>)
        });

        return (
        <div className="list card" >
          <div className="item row">
            <div  className="col margin">
              <h2>{advert.type}</h2>
              <p>{advert.cost}</p>
            </div>
            <div className="col">
              <p>{advert.address}</p>
            </div>
          </div>
          <div className="item item-body">
            <div className="slidebox">
                <div className="slides row" id={advert.slider}>{images}</div>
            </div>
            <p>{advert.description}</p>
            <p>{numbers}</p>
          </div>
            <div className="item tabs tabs-secondary tabs-icon-left" onClick={scope.addToBookmark(advert)}>
                <div  className="tab-item">
                    <i className="ion-android-promotion"></i>
                    {(advert.bookmark === true) ? ' Убрать из закладок' : " Добавить в закладки"}
                </div>
            </div>

        </div>
        );
    });

    return (
    <div>
    {items}
    </div>
    );
  }
});



