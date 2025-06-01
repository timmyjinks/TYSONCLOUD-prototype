import { redirect, fail } from '@sveltejs/kit';

export const actions = {
	update: async ({ request }) => {
		const formData = await request.formData();
		const new_name= formData.get('new_name').replace(/[^a-zA-Z0-9-_]/g, '') as string;
		const image = formData.get('image').replace(/[^a-zA-Z]/g, '') as string;
		const update_image = formData.get('update_image');
		const id = formData.get('id');

		const response = await fetch('http://localhost:8000/container', {
			method: 'PUT',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				new_name: new_name,
				image: image,
        update_image: update_image,
        id: id,
			})
		});
    
    if(response.status == 200) {
		  throw redirect(303, '/containers');
    } else {
      return fail(400, {
        error: "Error updating container"
      })
    }
	},
	delete: async ({ request }) => {
		const formData = await request.formData();
    const id = formData.get("id");

    console.log(id);


    const response = await fetch("http://localhost:8000/container", 
    {
      method: "DELETE",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        id: id,
      },
      ) 
    }  
  )

    if(response.status == 200) {
		  throw redirect(303, '/containers');
    } else {
      return fail(400, {
        error: "Error deleting container"
      })
    }
	},
};
