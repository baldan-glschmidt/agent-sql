# R303CES

## Descrição

e-Sfinge - Concursos/Especialidade

---

## Resumo

- Campos: 14
- Chave Primária: 8 campo(s)
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
| Especi | Number(006,0) | Não | Número da especialidade |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CodCar | String(016) | Não | Código do cargo atribuído pela unidade |
| VigCar | Date | Não | Data de Início da Vigência do Cargo |
| DesEsp | String(100) | Não | Descrição da especialidade |
| QtdVag | Number(006,0) | Não | Quantidade de vagas oferecidas no concurso |
| DtHomo | Date | Sim | Data de homologação da especialidade |
| ValVen | Number(014,2) | Não | Valor da previsão do vencimento |
| DesHab | String(255) | Sim | Descrição da habilitação exigida para a especialidade |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- Edital
- Especi
- TipQua
- CodCar
- VigCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
