export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building && !(this.evacuationWarningMessage)) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this.sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    if (typeof newSqft !== 'number') {
      throw new TypeError('Sqft must be a number');
    } else {
      this._sqft = newSqft;
    }
  }
}
