# E085IMG

## Descrição

Cadastros - Clientes - Imagens

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
| CodCli | Number(009,0) | Não | Código do cliente |
| SeqImg | Number(005,0) | Não | Sequência da Imagem |
| DesImg | String(100) | Não | Descrição do que a imagem significa |
| TipDic | Number(001,0) | Sim | Tipo Imagem |
| ImgRef | Image | Sim | Imagem |
| DatImg | Date | Sim | Data da Imagem |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodCli
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E085IMG_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

