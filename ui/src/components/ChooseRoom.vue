<script setup lang="ts">
import { useRouter } from 'vue-router';
import { getRooms } from '../rooms';

const rooms = getRooms();

const router = useRouter();

const selectRoom = (id: string) => {
    router.push(`/${id}`);
};
</script>

<template>
    <div class="rooms">
        <div v-for="room in rooms" :key="room.id" class="room" @click="selectRoom(room.id)">
            <img :src="room.image" alt="" class="room-image">
            <div class="room-name">{{ room.name }}</div>
        </div>
    </div>
</template>

<style scoped>
.rooms {
    display: flex;
    justify-content: center;
    gap: 20px;
}

.room {
    cursor: pointer;
    transition: transform 0.2s;
}

.room:hover {
    transform: scale(1.1);
    filter: drop-shadow(0 0 2em #646cffaa);
}

.room-image {
    border-radius: 50%;
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
}

.room-name {
    margin-top: 10px;
}
</style>
