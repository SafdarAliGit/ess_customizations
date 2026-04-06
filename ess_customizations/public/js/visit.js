frappe.ui.form.on('Visit', {

    refresh(frm) {
        setTimeout(() => {
            frm.trigger('sync_location_to_map');
        }, 800);
    },

    location(frm) {
        setTimeout(() => {
            frm.trigger('sync_location_to_map');
        }, 300);
    },

    sync_location_to_map(frm) {
        const loc = frm.doc.location;
        if (!loc || !loc.includes(',')) return;

        const [lat, lng] = loc.split(',').map(parseFloat);
        if (isNaN(lat) || isNaN(lng)) return;

        const geoValue = JSON.stringify({
            type: "FeatureCollection",
            features: [{
                type: "Feature",
                properties: {},
                geometry: {
                    type: "Point",
                    coordinates: [lng, lat]   // GeoJSON = [lng, lat]
                }
            }]
        });

        // Set value on the doc directly and refresh the field
        frm.doc.custom_map = geoValue;
        frm.get_field('custom_map').set_value(geoValue);
        frm.refresh_field('custom_map');

        // After field re-renders, zoom into the point
        setTimeout(() => {
            const field = frm.get_field('custom_map');
            if (!field || !field.map) return;

            field.map.setView([lat, lng], 15);

        }, 600);
    }

});