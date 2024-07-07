<script>
  import { onMount } from 'svelte';

  let data;
  let error = null;

  onMount(async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/adherents');

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const jsonData = await response.json();
      data = jsonData;
      console.log(data);
    } catch (err) {
      console.error('Fetch error: ', err);
      error = err.message;
    }
  });
</script>

<div>
  {#if error}
    <p>Erreur: {error}</p>
  {/if}
  {#if data}
    <ul>
      {#each data as adherent}
        <li key={adherent.id}>{adherent.name}</li>
      {/each}
    </ul>
  {/if}
</div>
