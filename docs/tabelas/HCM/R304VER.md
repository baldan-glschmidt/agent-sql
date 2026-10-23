# R304VER

## Descrição

e-Sfinge Online - Tabela de versões

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| VerEsf | String(010) | Não | Versão do artefato eSfinge |
| TipVer | Number(002,0) | Não | Tipo de artefato versionado |
| DatIni | Date | Não | Data de início da vigência da versão do artefato |
| DatGr1 | Date | Sim | Data de início da vigência do grupo 1, pós início da versão do artefato |
| DatGr2 | Date | Sim | Data de início da vigência do grupo 2, pós início da versão do artefato |
| DiaCar | Number(002,0) | Sim | Qtde de dias de carência para alterar nível de severidade das consistências |
| DatAtu | Date | Sim | Data do primeiro envio após a atualização de versão |
| CmpAu1 | Date | Sim | Campo Auxiliar 1 |
| CmpAu2 | Date | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(008,0) | Sim | Campo Auxiliar 3 |

---

## Chave Primária

- VerEsf
- TipVer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
