# R031STU

## Descrição

Geração de Escalas - Símbolos Por Turno

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTur | Number(001,0) | Não | Código do Turno |
| CodSib | Number(003,0) | Não | Código do Símbolo |
| DiaFol | Number(003,0) | Sim | Símbolo Dia de Folga |
| DiaTrb | Number(003,0) | Sim | Símbolo Dia de Trabalho |
| DiaDup | Number(003,0) | Sim | Símbolo Dia de Turno Duplo |
| DiaFEs | Number(003,0) | Sim | Símbolo Dia de Folga Especial |
| DiaTDF | Number(003,0) | Sim | Símbolo Dia de Turno Duplo de Folga |
| DiaCom | Number(003,0) | Sim | Símbolo Dia Compensado/DSR |
| DiaTEs | Number(003,0) | Sim | Símbolo para Dia de Troca de Escala |

---

## Chave Primária

- CodTur
- CodSib

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R031STU_001

**Tabela:** R031SIB

| Origem | Destino |
|--------|---------|
| CodSib | CodSib |

