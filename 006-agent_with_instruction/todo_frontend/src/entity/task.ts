/**
 * タスク
 */
export interface Task {
    id?: number;
    text: string;
    done?: boolean;
    createdAt?: string; // ISO8601形式の文字列
    completedAt?: string; // ISO8601形式の文字列
}
