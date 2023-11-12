<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { getRoom, ControlGroup } from '../rooms';

import Control from './Control.vue'

const route = useRoute();
const roomControls = ref<ControlGroup[]>([]);
const roomImage = ref<string>('');
const roomTitle = ref<string>('');

onMounted(async () => {
    const roomId = route.params.id as string;
    const room = getRoom(roomId);
    roomControls.value = room.controls;
    roomImage.value = room.image;
    roomTitle.value = room.title;
});
</script>

<template>
    <h2>{{ roomTitle }}</h2>
    <img :src="roomImage" alt="" class="room-image" />

    <div class="room-groups">
        <div v-for="controlGroup in roomControls" :key="controlGroup.title" class="control-group">
            <h3>{{ controlGroup.title }}</h3>
            <div class="controls">
                <Control v-for="control in controlGroup.values" :value="control" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.room-image {
    border-radius: 50%;
    height: 12em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
}

.room-groups {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.control-group {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.controls {
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 5px;
}
</style>
