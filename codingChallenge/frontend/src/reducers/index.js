import {
  combineReducers
} from "redux";
import recipes from "./recipes";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";

export default combineReducers({
  recipes,
  errors,
  messages,
  auth
});