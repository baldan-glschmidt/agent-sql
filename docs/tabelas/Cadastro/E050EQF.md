# E050EQF

## Descrição

Tabelas - Impostos - Equipamentos Fiscais

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodEqu | Number(003,0) | Não | Código do equipamento fiscal |
| DesEqu | String(050) | Não | Descrição do equipamento fiscal |
| TipEqf | Number(001,0) | Não | Indicador do tipo de equipamento fiscal |
| NumSer | String(025) | Não | Número de série do equipamento fiscal |
| NumFab | String(020) | Sim | Número de fabricação do ECF |
| LinMad | String(001) | Sim | Letra indicativa MF adicional do ECF |
| TipEcf | String(007) | Sim | Tipo de ECF |
| MarEcf | String(020) | Sim | Marca do ECF |
| ModEcf | String(020) | Sim | Modelo de ECF |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |

---

## Chave Primária

- CodEmp
- CodFil
- CodEqu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
