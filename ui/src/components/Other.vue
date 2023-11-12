<script setup lang="ts">
import { ref, watch, onMounted } from 'vue';
import { getRoom, ControlValue, ControlType } from '../rooms';
import { executeTask, getDevices, getProperty, getTasks } from '../services/api'

import Control from './Control.vue'

const roomImage = ref<string>('');
const roomTitle = ref<string>('');
const devices = ref<string[]>([]);
const tasks = ref<string[]>([]);
const currentDevice = ref<string>();
const currentTask = ref<string>();
const deviceControlValue = ref<ControlValue>();

onMounted(async () => {
    const room = getRoom("other");
    roomImage.value = room.image;
    roomTitle.value = room.title;
    devices.value = (await getDevices()).data.values.filter((v: string) =>
        v.startsWith('LT') || v.startsWith('TR') || v.startsWith('DM')
    );
    tasks.value = (await getTasks()).data.values;
});

watch(currentDevice, async (value) => {
    if (value == null) {
        return;
    }

    let originalType: string = (await getProperty(value, 'TControl Type')).data.value;
    let typesDict: { [key: string]: ControlType; } = {
        "LT8": "switch",
        "TR4": "shutter",
        "DM4": "dimmer",
    };
    let currentType = typesDict[originalType] || null;

    if (currentType == null) {
        return;
    }

    deviceControlValue.value = {
        title: value,
        type: currentType,
        id: value,
    }
});

const onRunTaskClick = () => {
    if (currentTask.value == null) {
        return;
    }

    executeTask(currentTask.value);
}
</script>

<template>
    <h2>{{ roomTitle }}</h2>
    <img :src="roomImage" alt="" class="room-image" />

    <div class="room-groups">
        <div class="control-group">
            <h3>מכשירים</h3>
            <v-select :options="devices" v-model="currentDevice"></v-select>
            <Control v-if="deviceControlValue != null" :value="deviceControlValue" />
        </div>
        <div class="control-group">
            <h3>פעולות</h3>
            <v-select :options="tasks" v-model="currentTask"></v-select>
            <button v-if="currentTask != null" @click="onRunTaskClick">
                הפעל
            </button>
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
</style>
