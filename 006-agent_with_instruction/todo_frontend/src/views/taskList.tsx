import { Task } from "../entity/task";
import * as api from "../api/task";

interface ListTaskViewProps {
    taskList: Task[];
    reloadTasks: () => Promise<void>;
}

export const ListTaskView = (props: ListTaskViewProps) => {
    const cards = props.taskList.map((task) => (
        <TaskCard
            task={task}
            reloadTasks={props.reloadTasks}
            key={task.id}
        ></TaskCard>
    ));
    return <div className="row p-2">{cards}</div>;
};

interface TaskCardProps {
    task: Task;
    reloadTasks: () => Promise<void>;
}

const TaskCard = (props: TaskCardProps) => {
    async function clickDone(): Promise<void> {
        await api.postTaskDone(props.task);
        props.reloadTasks();
    }

    // 日付を見やすい形式に変換
    const formatDate = (iso?: string) => {
        if (!iso) return "";
        const d = new Date(iso);
        return d.toLocaleString();
    };

    return (
        <div className="card m-2" style={{ width: "28rem" }}>
            <div className="card-body">
                <h5 className="card-title">{props.task.id}</h5>
                <p className="card-text">{props.task.text}</p>
                <div className="mb-2">
                    <small className="text-muted">作成日: {formatDate(props.task.createdAt)}</small><br />
                    <small className="text-muted">完了日: {formatDate(props.task.completedAt)}</small>
                </div>
                <button className="btn btn-primary" onClick={clickDone}>
                    done
                </button>
            </div>
        </div>
    );
};
