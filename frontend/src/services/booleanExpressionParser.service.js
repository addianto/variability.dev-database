import {Negation} from "@/classes/Constraint/Negation";
import {Implication} from "@/classes/Constraint/Implication";
import {Conjunction} from "@/classes/Constraint/Conjunction";
import {Disjunction} from "@/classes/Constraint/Disjunction";
import {FeatureNodeConstraintItem} from "@/classes/Constraint/FeatureNodeConstraintItem";

const operators = ['not', 'and', 'or', 'implies'];
const operatorPrecedence = {};
operators.forEach((operator, i) => operatorPrecedence[operator] = i);

export function parse(toParse, allNodes) {
    const inputToken = toParse
        .replaceAll('(', '( ')
        .replaceAll(')', ' )')
        .split(' ')
        .filter((str) => str);

    const operatorStack = [];
    let outputStack = [];
    inputToken.forEach((token) => {
        if (operators.includes(token.toLowerCase())) {
            parseOperator(token.toLowerCase(), operatorStack, outputStack);
        } else if (token === '(') {
            operatorStack.push('(');
        } else if (token === ')') {
            parseClosingBracket(operatorStack, outputStack);
        } else {
            outputStack.push(createFeatureNodeConstraintItem(token, allNodes));
        }
    });

    // Push all operators that remains on operator-stack to output
    while (operatorStack.length) {
        convertToConstraintItem(operatorStack.pop(), outputStack);
    }

    return outputStack[0];
}

function parseOperator(token, operatorStack, outputStack) {
    if (operatorStack.length) {
        let lastOperator = operatorStack.at(-1);
        while (lastOperator && lastOperator !== '(' && operatorPrecedence[token] > operatorPrecedence[lastOperator]) {
            operatorStack.pop();
            convertToConstraintItem(lastOperator, outputStack);
            lastOperator = operatorStack.length ? operatorStack.at(-1) : undefined;
        }
    }
    operatorStack.push(token);
}

function parseClosingBracket(operatorStack, outputStack) {
    let lastOperator = operatorStack.pop();
    while (lastOperator !== '(' && operatorStack.length !== 0) {
        convertToConstraintItem(lastOperator, outputStack);
        lastOperator = operatorStack.pop();
    }
}

function convertToConstraintItem(operator, stack) {
    operator = operator.toLowerCase();
    let constraintItem = undefined;
    if (operator === 'not') {
        constraintItem = new Negation(stack.pop());
    } else if (operator === 'and') {
        const second = stack.pop();
        const first = stack.pop();
        constraintItem = new Conjunction(first, second);
    } else if (operator === 'or') {
        const second = stack.pop();
        const first = stack.pop();
        constraintItem = new Disjunction(first, second);
    } else if (operator === 'implies') {
        const conclusion = stack.pop();
        const premise = stack.pop();
        constraintItem = new Implication(premise, conclusion);
    }

    stack.push(constraintItem);
}

function createFeatureNodeConstraintItem(featureNodeName, allNodes) {
    const foundNode = allNodes.find((node) => node.name === featureNodeName);
    if (!foundNode) {
        console.error('constraint-parser', featureNodeName + ' was not found');
    }
    return new FeatureNodeConstraintItem(foundNode);
}