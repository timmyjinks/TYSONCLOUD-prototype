import type { PageServerLoad } from './$types';

export const load = (async ()  => {
  const response = await fetch("http://localhost:8000/containers")
  const data = await response.json()
  return {containers: data}
}) satisfies PageServerLoad;
 
