# E000CIX

## Descrição

Tabelas - Integrações - Controle de registros integrados

---

## Resumo

- Campos: 15
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodInt | Number(002,0) | Não | Código da Integração |
| IdeInt | Number(009,0) | Não | Código Identificador do tipo de informação |
| DatExp | Date | Sim | Data da última exportação dos dados |
| HorExp | Number(005,0) | Sim | Hora da última exportação dos dados |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração dos dados |
| SegAlt | Number(005,0) | Sim | Segundo e milissegundo da alteração |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| SitIex | String(001) | Sim | Situação do processamento da pendência de integração |
| MsgErr | String(998) | Sim | Mensagem de erro ocorrida no processamento |
| IndExp | String(001) | Sim | Indicativo de Exportação |
| NumLot | Number(009,0) | Sim | Número do lote gerado ao exportar o registro |
| VerReg | Number(009,0) | Sim | Versão do Registro |
| RegInt | String(001) | Sim | Indicativo de Registro Integrável |

---

## Chave Primária

- SeqInt
- CodInt
- IdeInt

---

## Índices

### E000CIXIndiceSistema

**Tipo:** Unico

Campos:
- IdeInt
- CodInt
- SeqInt
- SitIex

### E000CIXIndiceLote

**Tipo:** Não unico

Campos:
- CodInt
- IdeInt
- NumLot

---

## Relacionamentos

Nenhum relacionamento cadastrado.
