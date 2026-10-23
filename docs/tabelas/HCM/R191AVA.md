# R191AVA

## Descrição

Objetivos Coletivos - Identificação

---

## Resumo

- Campos: 16
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo de avaliação |
| SeqAva | Number(002,0) | Não | Sequência |
| DesIde | String(1999) | Sim | Descrição dos Objetivos Coletivos |
| TipPub | Number(001,0) | Sim | Tipo de público envolvido |
| AbrEmp | String(100) | Sim | Abrangência de Empresa |
| AbrFil | String(100) | Sim | Abrangência de Filial |
| AbrPos | String(100) | Sim | Abrangência de Posto |
| AbrCar | String(100) | Sim | Abrangência de Cargo |
| AbrLoc | String(1500) | Sim | Abrangência de Local |
| AbrCcu | String(100) | Sim | Abrangência de Centro de Custo |
| AbrTur | String(100) | Sim | Abrangência de Turno |
| AbrVin | String(100) | Sim | Abrangência de Vínculo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- TipAva
- SeqAva

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R191AVA_004

**Tabela:** R101CTA

| Origem | Destino |
|--------|---------|
| CodCic | CodCic |
| TipAva | TipAva |

