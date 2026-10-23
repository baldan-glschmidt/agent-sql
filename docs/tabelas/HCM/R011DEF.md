# R011DEF

## Descrição

Definição do Banco de Horas

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBhr | Number(005,0) | Não | Código do Banco de Horas |
| VerLim | String(001) | Sim | Verificar Limites do Banco de Horas |
| CmpBhr | Number(001,0) | Sim | Tipo de Compensação dos Lançamentos |
| CalEst | Number(001,0) | Sim | Calcular Estouro do Banco |
| CalEsM | Number(001,0) | Sim | Calcular Estouro Mensal |
| CalFec | String(001) | Sim | Calcular Fechamento |
| PrrAfa | String(001) | Sim | Prorrogar Banco de Horas nos Afastamentos |
| SitCre | Number(003,0) | Sim | Situação de crédito para transferência |
| SitDeb | Number(003,0) | Sim | Situação de débito para transferência |
| ConPme | String(001) | Sim | Considerar primeiro fechamento na prorrogação |
| TmpPro | Number(001,0) | Sim | Tempo de Prorrogação |
| VerPro | Number(001,0) | Sim | Verificar afastamentos para prorrogação |

---

## Chave Primária

- CodBhr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R011DEF_000

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBhr | CodBHr |

