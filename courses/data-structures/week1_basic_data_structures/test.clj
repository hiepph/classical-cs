(require '[babashka.curl :as curl])
(require '[babashka.process :refer [process $ check]])

(if (empty? *command-line-args*) (println "Usage: bb -f test.clj <module>"))
(let [module (first *command-line-args*)
        files (file-seq (clojure.java.io/file module))
        main (str (first (filter
                          #(str/ends-with? (.getName %) ".py") files)))
        in-files (->> (filter
                       #(re-matches (re-pattern
                                     (format "%stests/%s" module #"\d+"))
                                    (str %)) files)
                      (map str)
                      sort)]
    (doseq [in-file (take 10 in-files)
          :let [out-file (format "%s.a" in-file)
                input (->> in-file slurp str/trim)
                output (->> out-file slurp str/trim)]]
      (let [res (-> (process ["cat"] {:in input
                                   :val :string})
                 (process (conj '[python] main))
                 :out
                 slurp
                 str/trim)]
        (if-not (= output res)
          (throw (AssertionError.
                  (format "\nin:\n%s\nout: %s\ngot: %s"
                          input output res))))))
    "Test succeeded")
