# E075PCB

## Descrição

Cadastros - Produtos - Percentual Origem

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodUfo | String(002) | Não | Código da UF origem |
| DatIni | Date | Não | Data de início de vigência |
| MotRmo | Number(002,0) | Sim | Motivo de redução de Alíquota de ICMS Monofásico |
| IndImp | String(001) | Sim | Indicador de Importação |
| PerOri | Number(007,4) | Sim | Percentual Originário para a UF |
| CodFil | Number(005,0) | Sim | Código da filial |

---

## Chave Primária

- CodEmp
- CodPro
- CodUfo
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
