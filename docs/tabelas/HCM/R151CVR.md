# R151CVR

## Descrição

Credencial Ativa do Visitante com Acesso a Recinto Aduaneiro

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
| TipDoc | Number(001,0) | Não | Tipo do Documento do Visitante |
| NumDoc | String(020) | Não | Número do Documento do Visitante |
| VerPlf | Number(003,0) | Não | Versão do plano de localização física do recinto aduaneiro |
| CodPlf | Number(007,0) | Não | Código do local físico do recinto aduaneiro |
| CodRec | Number(015,0) | Sim | Código do recinto aduaneiro |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatIni | Date | Não | Data de início do uso do crachá |
| HorIni | Number(005,0) | Não | Hora de início do uso do crachá |
| DatFim | Date | Sim | Data Final do Uso do Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Uso do Crachá |
| SeqEnt | Number(002,0) | Não | Sequência do Registro |
| Repres | String(001) | Sim | Enviar como Representado para a API-Recintos, através do evento Representantes |
| Protcl | String(036) | Sim | Protocolo do evento retornado pela ADE-02 |
| StaAlf | Number(001,0) | Não | Status da permissão para o local alfandegado, por recinto |
| StaRec | Number(001,0) | Não | Status do histórico do recinto aduaneiro |

---

## Chave Primária

- CodPen

---

## Índices

### R151CVRIndice2

**Tipo:** Não unico

Campos:
- TipDoc
- NumDoc
- DatIni
- HorIni

### R151CVRIndice3

**Tipo:** Não unico

Campos:
- TipDoc
- NumDoc
- VerPlf
- CodPlf
- DatIni
- HorIni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
