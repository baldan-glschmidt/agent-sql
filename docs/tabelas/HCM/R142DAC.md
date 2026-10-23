# R142DAC

## Descrição

Diagnósticos Treinamento - Ações

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDia | Number(009,0) | Não | Código do Diagnóstico |
| SeqDac | Number(002,0) | Não | Sequência do Registro |
| CodPar | Number(003,0) | Sim | Parecer sobre a Ação proposta |
| DesDac | String(150) | Sim | Descrição da Ação Proposta |
| ComDac | String(150) | Sim | Comentário sobre a Ação proposta |

---

## Chave Primária

- CodDia
- SeqDac

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R142DAC_000

**Tabela:** R142DIA

| Origem | Destino |
|--------|---------|
| CodDia | CodDia |

