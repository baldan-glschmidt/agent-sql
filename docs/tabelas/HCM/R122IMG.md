# R122IMG

## Descrição

Candidatos Externos - Imagens

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| SeqImg | Number(003,0) | Não | Sequência de imagem |
| TipDoc | Number(004,0) | Sim | Tipo da imagem |
| ObsImg | String(499) | Sim | Observação |
| Imagem | Image | Sim | Imagem |
| NomArq | String(250) | Sim | Nome do Arquivo |
| CodRqu | Number(009,0) | Sim | Código Requisição |

---

## Chave Primária

- NumCan
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122IMG_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122IMG_002

**Tabela:** R022DOC

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |

