# R303CON

## Descrição

e-Sfinge - Concursos/Concurso

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano |
| BimAno | Number(001,0) | Não | Código Bimestre Ano |
| Edital | String(016) | Não | Número do edital de concurso |
| TEdCon | Number(002,0) | Não | Tipo de edital |
| DtHomR | Date | Não | Data em que foi homologado o resultado final do concurso |
| DtValC | Date | Não | Data de validade do concurso |
| DtPrrC | Date | Sim | Data prorrogável do concurso |
| PVgPcD | Number(006,3) | Não | Percentual de vagas para portador de deficiências |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- Edital

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
