import { redirect, fail } from '@sveltejs/kit';

export const actions = {
	create: async ({ request }) => {
		const formData = await request.formData();
		const name = formData.get('name');
		const image = formData.get('image');
    const github = formData('github');
		const enable_github = formData.get('enable_github');

		const response = await fetch('http://localhost:8000/containers', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				name: name,
				image: image,
				github: github,
				enable_github: enable_github,
			})
		});

    if(response.status == 200) {
		  throw redirect(303, '/containers');
    } else {
      return fail(400, {
        error: "Error creating container"
      })
    }
	},
};
