# R303PAC

## Descrição

e-Sfinge - Plano de Cargos/Atualização do Cargo ou Função

---

## Resumo

- Campos: 16
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano |
| BimAno | Number(001,0) | Não | Código Bimestre Ano |
| TipAtu | Number(002,0) | Não | Tipo de atualização |
| TTxJur | Number(002,0) | Não | Tipo do texto jurídico |
| NmTxJr | Number(016,0) | Não | Número do texto jurídico que atualizou o plano de cargos |
| TipQua | Number(002,0) | Não | Tipo de Quadro |
| CodCar | String(016) | Não | Código do cargo ou função atribuído pela unidade |
| VigCar | Date | Não | Data de Início da Vigência do Cargo |
| NomCar | String(100) | Sim | Nome do cargo ou função |
| FimVig | Date | Sim | Data em que o cargo ou função deixou de viger |
| TipCar | Number(002,0) | Sim | Tipo de cargo ou função |
| DesCHr | String(020) | Sim | Descrição da carga horária |
| QtdCHr | Number(007,0) | Sim | Quantidade numérica conforme a carga horária descrita |
| TpCAcu | Number(002,0) | Sim | Tipo de cargo para fins de acumulação |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- TipAtu
- TTxJur
- NmTxJr
- TipQua
- CodCar
- VigCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
