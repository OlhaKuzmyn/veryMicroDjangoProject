import {IProfile} from "./profile.interface";

export interface IUser {
    email: string,
    password: string,
    is_dm: boolean,
    profile: IProfile
}
