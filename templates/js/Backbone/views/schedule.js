var itin = new itinerary();
var schedule = Backbone.View.extend({
	el: '#schedule',
	initialize: function(){
		itin.on('add', this.showAll);
		itin.fetch();
	}, 
	showAll: function(Pmodel){
		var Sview = new AppointmentView({model:Pmodel});
		$('.view').append(Sview.render().$el);
	}
});

var AppointmentView = Backbone.View.extend({
	template: _.template($('#scheduler').html()),
	render: function(){
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

var it = new schedule();
