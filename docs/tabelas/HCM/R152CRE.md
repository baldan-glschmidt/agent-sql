# R152CRE

## Descrição

Tabela de detalhe de pendência do evento Credenciamento de Pessoas

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 4
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPen | Number(018,0) | Não | Código do detalhe da pendência de Recintos Aduaneiros |
| TipPes | Number(001,0) | Não | Tipo da pessoa detentora da credencial |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| DatIni | Date | Sim | Data de início do uso do crachá |
| HorIni | Number(005,0) | Sim | Hora de início do uso do crachá |
| TipCra | Number(001,0) | Sim | Tipo de crachá - crachá de colaborador |
| SeqEnt | Number(002,0) | Sim | Sequência do registro - crachá de Visitante |
| JSON | String(4000) | Sim | JSON do evento de Controle de Acesso de Pessoas |
| ProOri | String(036) | Sim | Protocolo do evento retornado pela ADE-02, em casos de exclusão do reg. original |

---

## Chave Primária

- CodPen

---

## Índices

### R152CREIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

### R152CREIndice3

**Tipo:** Não unico

Campos:
- TipDoc
- NumDoc

### R152CREIndice4

**Tipo:** Não unico

Campos:
- TipCra
- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

### R152CREIndice5

**Tipo:** Não unico

Campos:
- TipDoc
- NumDoc
- DatIni
- HorIni
- SeqEnt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
