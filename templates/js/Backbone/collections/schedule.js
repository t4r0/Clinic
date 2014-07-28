var itinerary = Backbone.Collection.extend({
	model: Appointment,
	url:'/api/v/appointment'
});