import roomsData from './assets/rooms.json';

export type ControlType = 'switch' | 'shutter' | 'dimmer';

export type ControlValue = {
    title: string;
    type: ControlType;
    id: string;
};

export type ControlGroup = {
    title: string;
    values: ControlValue[];
};

export type Room = {
    title: string;
    image: string;
    controls: ControlGroup[];
};

export type RoomsData = {
    [key: string]: Room;
};


const typedRoomsData = roomsData as RoomsData;

export const getRoom = (roomId: string): Room => {
    return typedRoomsData[roomId] || [];
};

export const getRooms = () => {
    return Object.entries(typedRoomsData).map(([id, room]) => ({
        id,
        name: room.title,
        image: room.image,
    })); ``
};
