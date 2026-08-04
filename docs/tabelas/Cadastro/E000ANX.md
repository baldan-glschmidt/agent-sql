# E000ANX

## Descrição

Tabelas - Controle de arquivos anexos

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| RotAnx | Number(002,0) | Não | Código da rotina para controle de arquivos anexos |
| NumAnx | Number(010,0) | Não | Número do controle de arquivos anexos gerado pelo sistema |
| SeqAnx | Number(004,0) | Não | Seq. de inclusão dos arquivos anexos |
| DesAnx | String(050) | Não | Descrição do arquivo anexo |
| LocAnx | String(250) | Não | Localização do documento anexo |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização |
| TipAnx | Number(001,0) | Sim | Tipo do anexo |
| ValAnx | Date | Sim | Validade do documento anexo |

---

## Chave Primária

- CodEmp
- RotAnx
- NumAnx
- SeqAnx

---

## Índices

### E000ANXIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- RotAnx
- NumAnx

---

## Relacionamentos

Nenhum relacionamento cadastrado.
