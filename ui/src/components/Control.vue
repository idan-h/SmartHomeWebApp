<script setup lang="ts">
import { ref, toRef, watchEffect } from 'vue';
import { ControlValue } from '../rooms'
import { setProperty, getProperty } from '../services/api'

const props = defineProps({
    value: {
        type: Object as () => ControlValue,
        required: true
    }
});

const value = toRef(props, 'value');

const isSwitchOn = ref(false);
const dimmerValue = ref(null);

const updateControlState = async () => {
    switch (value.value.type) {
        case 'switch':
            let propVal;
            while (true) {
                propVal = (await getProperty(value.value.id, 'TControl Switch Command')).data.value;

                if (propVal != 'Toggle') {
                    break;
                }

                await new Promise(resolve => setTimeout(resolve, 500));
            }
            isSwitchOn.value = propVal == 'On'
            break;
        case 'dimmer':
            dimmerValue.value = (await getProperty(value.value.id, 'TControl Dimmer Target Level')).data.value;
            break;
    }
}

watchEffect(() => {
    return updateControlState();
});

const toggleSwitch = async (id: string) => {
    isSwitchOn.value = !isSwitchOn.value;
    await setProperty(id, 'TControl Switch Command', 'Toggle');
    updateControlState();
}

const dimmerValueChange = async (v: number) => {
    await setProperty(value.value.id, 'TControl Dimmer Target Level', v.toString());
}
</script>

<template>
    <div v-if="value.type === 'switch'">
        <button v-on:click="toggleSwitch(value.id)" :class="{ 'light-on': isSwitchOn }">
            {{ value.title }}
        </button>
    </div>
    <div v-else-if="value.type === 'shutter'" class="shutter-control">
        <button v-on:click="setProperty(value.id, 'TControl Shutter Command', 'Up')">
            ↑
        </button>
        <button v-on:click="setProperty(value.id, 'TControl Shutter Command', 'Stop')" class="shutter-title">
            {{ value.title }}
        </button>
        <button v-on:click="setProperty(value.id, 'TControl Shutter Command', 'Down')">
            ↓
        </button>
    </div>
    <div v-else-if="value.type === 'dimmer'">
        {{ value.title }}
        <v-slider v-model="dimmerValue" @change="dimmerValueChange" />
    </div>
</template>

<style scoped>
.shutter-control {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

.shutter-title {
    text-align: center;
}

.light-on {
    background-color: #4d62de;
}
</style>
