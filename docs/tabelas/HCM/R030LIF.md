# R030LIF

## Descrição

Filiais - Liminares

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpLim | Date | Não | Competência da Liminar |
| CodLim | Number(002,0) | Não | Código da Liminar |
| DesLim | String(040) | Sim | Descrição da Liminar |
| CmpTer | Date | Sim | Competência Término da Liminar |
| AplEmp | String(001) | Sim | Aplicação da Liminar no Cálculo da Parte Empresa |
| AplRAT | String(001) | Sim | Aplicação da Liminar no Cálculo do RAT |
| AplTer | String(001) | Sim | Aplicação da Liminar no Cálculo de Terceiros/Outras Entidades |
| TipLim | Number(001,0) | Sim | Tipo da Liminar |
| CodPro | Number(009,0) | Sim | Código do Processo |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| ExtDec | Number(001,0) | Sim | Ext. da Decisão/Sentença que determina não incidência de contrib. previdenciária |
| BasLim | Number(001,0) | Sim | Composição Base Liminar |

---

## Chave Primária

- NumEmp
- CodFil
- CmpLim
- CodLim

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030LIF_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

