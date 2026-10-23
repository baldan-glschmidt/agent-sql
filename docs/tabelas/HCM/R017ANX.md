# R017ANX

## Descrição

Posto de Trabalho - Anexos

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| SeqAne | Number(002,0) | Não | Sequência do anexo |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| DesAne | String(060) | Sim | Descrição do arquivo anexo |
| ArqAne | Image | Sim | Arquivo anexo |

---

## Chave Primária

- EstPos
- PosTra
- SeqAne

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017ANX_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

