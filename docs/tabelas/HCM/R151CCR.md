# R151CCR

## Descrição

Credencial Ativa do Colaborador com Acesso a Recinto Aduaneiro

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPen | Number(018,0) | Não | Código do detalhe da pendência de Recintos Aduaneiros |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| VerPlf | Number(003,0) | Não | Versão do plano de localização física do recinto aduaneiro |
| CodPlf | Number(007,0) | Não | Código do local físico do recinto aduaneiro |
| CodRec | Number(015,0) | Sim | Código do recinto aduaneiro |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatIni | Date | Não | Data de início do uso do crachá |
| HorIni | Number(005,0) | Não | Hora de início do uso do crachá |
| DatFim | Date | Sim | Data Final do Uso do Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Uso do Crachá |
| TipCra | Number(001,0) | Não | Tipo de Crachá |
| Protcl | String(036) | Sim | Protocolo do evento retornado pela ADE-02 |
| StaAlf | Number(001,0) | Não | Status da permissão para o local alfandegado, por recinto |
| StaRec | Number(001,0) | Não | Status do histórico do recinto aduaneiro |

---

## Chave Primária

- CodPen

---

## Índices

### R151CCRIndice2

**Tipo:** Não unico

Campos:
- TipCra
- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

### R151CCRIndice3

**Tipo:** Não unico

Campos:
- TipCra
- NumEmp
- TipCol
- NumCad
- VerPlf
- CodPlf
- DatIni
- HorIni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
