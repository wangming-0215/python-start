// 获取今日预定的用户id列表
function getTodayUsers(callback) {
	setTimeout(() => {
		const users = [1, 2, 3, 4, 5];
		callback(users);
	}, 1000);
}

// 获取今日推荐的电影id
function getTodayMovie(callback) {
	setTimeout(() => {
		const movieId = 123;
		callback(movieId);
	}, 1000);
}

// 使用用户列表预定电影
function bookTodayMovieForUsers(userIds, movieId, callback) {
	setTimeout(() => {
		callback('订阅成功');
	}, 1000);
}

// 为今天预定的用户订阅今日推荐的电影
function bookTodayMovieForTodayUsers() {
	const usersPromise = promisify(getTodayUsers);
	const moviePromise = promisify(getTodayMovie);
	const bookTodayMovieForUsersPromise = promisify(bookTodayMovieForUsers);
	return Promise.all([usersPromise(), moviePromise()]).then(args => {
		const [userIds, movieId] = args;
		return bookTodayMovieForUsersPromise(userIds, movieId);
	});
}

function promisify(asyncFunc) {
	return function promisied(...args) {
		return new Promise((resolve, reject) => {
			asyncFunc(...args, arg => {
				resolve(arg);
			});
		});
	};
}

bookTodayMovieForTodayUsers().then(msg => console.log(msg));
