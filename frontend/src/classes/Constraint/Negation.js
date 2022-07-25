import {ConstraintItem} from "@/classes/Constraint/ConstraintItem";

export class Negation extends ConstraintItem {
    constructor(item) {
        super();
        this.item = item;
    }

    count() {
        return 1;
    }

    toString() {
        return `¬${this.addPossibleBrackets(this.item)}`;
    }

    toStringPostfix() {
        return `${this.item.toStringPostfix()} Negation`;
    }

    toStringXML() {
        return `<not>${this.item.toStringXML()}</not>`;
    }

    getFeatureNodes() {
        return this.item.getFeatureNodes();
    }
}