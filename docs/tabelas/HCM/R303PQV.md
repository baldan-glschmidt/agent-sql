# R303PQV

## Descrição

e-Sfinge - Plano de Cargos/Quadro de Vagas

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano |
| BimAno | Number(001,0) | Não | Código Bimestre Ano |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CodCar | String(016) | Não | Código do Cargo |
| VigCar | Date | Não | Data de Início da Vigência do Cargo |
| QtdVOc | Number(008,0) | Sim | Quantidade vagas ocupadas |
| QtdFxL | Number(008,0) | Sim | Quantidade fixada em lei |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- TipQua
- CodCar
- VigCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
